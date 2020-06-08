import random

# returns cost list of list of generators
# given by equation cost = aP^2 + bP + c
def cost_vector(P, A, B, C):
    num_gen = len(P)
    Cost = [0 for _ in range(num_gen)]

    for gi in range(num_gen):
        p, a, b, c = P[gi], A[gi], B[gi], C[gi]
        Cost[gi] = a*p**2 + b*p + c

    return Cost

# mock algorithm for testing gui
def mock_algorithm(P_min, P_max, p_load, p_loss, A, B, C, max_iter = 10000):
    n_g = len(P_min)
    return (random.sample(range(1, 1000), n_g), max_iter / 2, 1.14, 7.62, 0.3)


# method to solve Economic dispatching using Active Set method (Quadratic programming)

def run_algorithm(P_min, P_max, p_load, p_loss, A, B, C, max_iter = 10000):
    return mock_algorithm(P_min, P_max, p_load, p_loss, A, B, C, max_iter = 10000)