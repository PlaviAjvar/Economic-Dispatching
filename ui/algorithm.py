import random
import math
import numpy as np

# returns cost list of list of generators
# given by equation cost = aP^2 + bP + c
def cost_vector(P, A, B, C):
    num_gen = len(P)
    Cost = [0 for _ in range(num_gen)]

    for gi in range(num_gen):
        p, a, b, c = P[gi], A[gi], B[gi], C[gi]
        Cost[gi] = a*p**2 + b*p + c

    return Cost

######################################################
# Algorithm that solves Economic dispatching problem

# Uses Active Set method (Quadratic programming)
######################################################



#######################
# Form of the problem
#######################

# Problem is of the form: 
# min sum_i(cost(i)) 
# s.t. constraints

# Or equivalently: 
# min sum_i(a(i)*p(i)^2 + b(i)*p(i) + c(i)) 
# s.t. constraints

# a(i), b(i), c(i) are parameters (constants) of the generator itself with the dimension of monetary cost per hour
# p(i) are the control variables, the powers the generators produce
# We can completely ignore c(i) since they add up to a constant (doesn't affect the minimum)

# We can write the goal function as J(x) = 0.5*(p^T)*H*p + (g^T)*p
# where p = [p(1) p(2) ... p(n)]^T

# The matrix H is a diagonal matrix, with 2a(i) on it's diagonals
# The vector g has b(i) as it's components

#######################
# Problem constraints
#######################

# The constraits are of the form:

# 1. 1 equality constraint (law of conservation of power): 
# sum_i(p(i)) = p_loss + p_load

# 2. n_g box inequality constraints (power production saturation):
# p_min(i) <= p(i) <= p_max(i)

def run_algorithm(P_min, P_max, p_load, p_loss, A, B, C, max_iter = 10000):
    # first find a feasible point
    n_g = len(P_min)
    P_init = feasible_point(P_min, P_max, p_load, p_loss)
    P = np.array([[e] for e in P_init], dtype=float)

    # also initialize the corresponding working set of (inequality) constraints
    W = []
    for i in range(n_g):
        if math.isclose(P[i], P_min[i]):
            W.append((i, P_min[i], False))
        elif math.isclose(P[i], P_max[i]):
            W.append((i, P_max[i], True))

    # form matrix H and vector g
    H = np.array([[0] * n_g for _ in range(n_g)], dtype=float)
    for i in range(n_g):
        H[i,i] = 2*A[i]
    g = np.array([[B[i]] for i in range(n_g)], dtype=float)
    epsilon = 1e-9

    for k in range(max_iter):
        # transform the minimization problem from over p to over dk
        # where dk = p_new - p_cur
        # to do this we need to calculate a helper value gk
        gk = H.dot(P) + g
        # find matrix corresponding to working set W(k)
        # the dimensions will be (n_g + 1) x n_g at most
        (Ak, b) = constraint_matrix(W, P_min, P_max, p_load, p_loss)

        # solve equality constrained quadratic programming subproblem to find descent direction
        (dk, lam) = QP_sub(Ak, H, gk)

        # if dk is near zero (all components within epsilon-zone around zero)
        if all(math.isclose(dk_e, 0) for dk_e in dk):
            # minimum lambda over the active inequality constraints and corresponding index
            n_act = len(W) + 1
            lam_min, q = min([(lam[i,0], i-1) for i in range(1, n_act)])

            # if the smallest lagrange multiplier is nonnegative, we are done
            if lam_min >= 0:
                P_final = [P[i, 0] for i in range(n_g)]
                total_cost = find_total_cost(P, H, g, C)
                total_power = p_loss + p_load

                return (P_final, k+1, total_cost, total_power, p_loss)
            # else we need to remove one of the active constraints
            else:
                # remove the constraint corresponding to the minimal (negative) lambda
                W = W[:q] + W[(q+1):]
        
        # otherwise we step in the direction of dk until we hit a barrier or converge
        else:
            # calculate maximum stepsize t such that moving along t*dk is feasible
            # also calculate blocking constraint (with index p)
            (t, p, is_up) = step_scaler(W, P, dk, P_min, P_max)
            P = P + t * dk

            # if t < 1, we have colided with a blocking constraint (or p != -1)
            # in that case add constraint to working set
            # if there are multiple they will all eventually be added
            if p != -1:
                if is_up:
                    W.append((p, P_max[p], True))
                else:
                    W.append((p, P_min[p], False))

    # if we've reached here then the max number of iterations has been exceded
    # return the current feasible point (best we can do) and max number of iterations + 1
    # -1 for all other parameters

    P_final = [P[i, 0] for i in range(n_g)]
    return (P_final, max_iter + 1, -1, -1, -1)


# helper function which finds total cost for given vector of generator powers P
# 0.5 p^T * H * p + g^T * p + c

def find_total_cost(P, H, g, C):
    quadratic = 0.5*np.transpose(P).dot(H.dot(P))
    linear = np.transpose(g).dot(P)
    constant = sum(C)
    return quadratic[0,0] + linear[0,0] + constant


# due to the nature of the constraints this is an easy problem
# however, the choce for the initial point can dramatically affect performance
# here we aren't using any fancy methods

def feasible_point(P_min, P_max, p_load, p_loss):
    # remaining power to be distributed
    p_remain = p_load + p_loss
    n_g = len(P_min)

    # difference between the powers (size of window)
    dP = [P_max[i] - P_min[i] for i in range(n_g)]
    # the output vector, all p(i) are at least p_min(i)
    P = [P_min[i] for i in range(n_g)]
    # first subtract all the P_min(i) from the power, since that much has to be used
    p_remain -= sum(P_min)

    # now use a greedy approach
    for i in range(n_g):
        # if there is remaining power to be distributed
        # then distribute as much as possible from the current generator
        if p_remain > 0:
            p_remained = p_remain
            p_remain -= min(p_remain, dP[i])
            P[i] += min(p_remained, dP[i])

    return P


# find the active constraint matrix
# also return the active rhs bounds for the equalities

def constraint_matrix(W, P_min, P_max, p_load, p_loss):
    n_g = len(P_min)
    num_act = len(W) + 1

    # initialize matrix
    A = np.array([[0] * n_g for _ in range(num_act)], dtype=float)
    b = np.array([[0] for _ in range(num_act)], dtype=float)

    # first row is always the one equality constraint
    # all ones becuase we are taking the sum of the pi's
    for i in range(n_g):
        A[0, i] = 1
    b[0, 0] = p_load + p_loss

    # depending if the constraint is <= or >= we change the sign
    # reduce everything to <= constraints
    for i, (k, v, is_up) in enumerate(W):
        if is_up:
            A[i + 1, k] = 1
            b[i + 1, 0] = v
        else:
            A[i + 1, k] = -1
            b[i + 1, 0] = -v
    
    return (A, b)

# equality constrained quadratic programming, closed form solution

# problem of the form:
# min 0.5*(x^T)*H*x + (g^T)*x
# s.t. A_k*x = 0

def QP_sub(Ak, H, g):
    # form new system matrix based on H and A, and form rhs of equation
    # dimensions will be 2*n_g x (n_g + n_act)
    n_act = len(Ak)
    n_g = len(H)

    # form closed form matrix equation
    A = closed_form_matrix(Ak, H, n_act, n_g)
    rhs = np.array([[-g[i,0]] if i < n_g else [0] for i in range(n_g + n_act)])

    # now solve system A * [x lambda]^T = [g 0]^T
    x = np.linalg.solve(A, rhs)
    d = x[: n_g]
    lam = x[n_g :]
    return (d, lam)


# helper function for calculating matrix for closed form constrained LS
# it's of the form [H Ak^T; Ak 0]

def closed_form_matrix(Ak, H, n_act, n_g):
    # A_up = [H Ak^T]
    A_up = np.hstack((H, np.transpose(Ak)))

    # A_down = [Ak 0]
    zeros = np.zeros((n_act, n_act), dtype=float)
    A_down = np.hstack((Ak, zeros))

    A = np.vstack((A_up, A_down))
    return A

# finds the step scaler t along a direction dk until a blocking constraint is hit
# also finds the index of the blocking constraint p

# for a given coordinate q: p_new(q) = p(q) + dk(q) * t
# p_min(q) <= p_new(q) <= p_max(q)

# p(q) + dk(q) * t <= p_max(q) ===> t <= (p_max(q) - p(q)) / dk(q)
# dk(q) > 0

# p(q) + dk(q) * t >= p_min(q) ===> t <= (p_min(q) - p(q)) / dk(q)
# dk(q) < 0

# The second conditions are imposed because if they aren't,
# the inequalities would be trivially satisfied for t > 0

def step_scaler(W, P, dk, P_min, P_max):
    # t is at most 1
    t = 1
    p = -1
    n_g = len(P_min)
    epsilon = 1e-9
    is_up = True

    # see which variables are fixed (in active constraints)
    is_active = [False for _ in range(n_g)]
    for (q, q_eq, is_q_up) in W:
        is_active[q] = True

    # iterate over all possible inequality constraints
    for i in range(n_g):
        if not is_active[i]:
            d = dk[i, 0]

            # the imposed conditions
            if d > epsilon and (P_max[i] - P[i][0]) / d < t:
                t =  (P_max[i] - P[i][0]) / d
                p = i
                is_up = True
            
            if d < -epsilon and (P_min[i] - P[i][0]) / d < t:
                t = (P_min[i] - P[i][0]) / d
                p = i
                is_up = False

    return (t, p, is_up)