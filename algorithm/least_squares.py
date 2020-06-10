import numpy as np
import scipy as sp
from algorithm import algorithm
from scipy import optimize

# used in optimization
def function(x):
    global H, g, c
    v = 0.5*np.transpose(x).dot(H.dot(x)) + np.transpose(g).dot(x) + c
    return v[0,0]

def run_algorithm(P_min, P_max, p_load, p_loss, A, B, C):
    global H, g, c

    n_g = len(P_min)
    # form matrix H and vector g
    H = np.array([[0] * n_g for _ in range(n_g)], dtype=float)
    for i in range(n_g):
        H[i,i] = 2*A[i]
    g = np.array([[B[i]] for i in range(n_g)], dtype=float)
    c = np.array([[sum(C)]])

    # box constraints
    box = [(P_min[i], P_max[i]) for i in range(n_g)]

    # equality constraint
    A = np.array([1 for _ in range(n_g)])
    p_tot = p_load + p_loss
    constr = optimize.LinearConstraint(A, np.array([p_tot]), np.array([p_tot]))
    # find feasible point
    x_init = algorithm.feasible_point(P_min, P_max, p_load, p_loss)
    x_0 = np.array([[e] for e in x_init])

    # optimize using generic solver
    optres = optimize.minimize(fun=function, x0=x_0, bounds=box, constraints=constr)
    P = [e for e in optres.x]
    iter_count = optres.status
    total_price = optres.fun
    total_power = p_load + p_loss
    total_power_loss = p_loss
    
    return (P, iter_count, total_price, total_power, total_power_loss)