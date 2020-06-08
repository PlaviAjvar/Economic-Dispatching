import random

# returns cost list of list of generators
# given by equation cost = aP^2 + bP + c
def cost(P, A, B, C):
    num_gen = len(P)
    Cost = [0 for _ in range(num_gen)]

    for gi in range(num_gen):
        p, a, b, c = P[gi], A[gi], B[gi], C[gi]
        Cost[gi] = a*p**2 + b*p + c

    return Cost

def run_algorithm(max_iter, P_min, P_max, P_load, P_loss, a, b, c):
    n_g = len(P_min)
    return (random.sample(range(1, 1000), n_g), max_iter / 2, 1.14, 7.62, 0.3)