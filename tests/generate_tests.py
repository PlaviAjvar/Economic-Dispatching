# dirty imports messing with path
import pathlib, sys
sys.path.insert(0, pathlib.Path().absolute())
print(pathlib.Path().absolute())

import random

if __name__ == "__main__":
    random.seed()

    for test in range(10):
        with open("input/test" + str(test) + ".txt", "w") as file:
            # number of generators
            if test < 3:
                n_g = 10
            elif test < 6:
                n_g = 100
            else:
                n_g = 250
            file.write(str(n_g) + "\n")

            P_min = [0.0 for _ in range(n_g)]
            P_max = [0.0 for _ in range(n_g)]
            A = [0.0 for _ in range(n_g)]
            B = [0.0 for _ in range(n_g)]
            C = [0.0 for _ in range(n_g)]

            P_tot_low = 0
            P_tot_high = 0

            # generate values randomly
            for i in range(n_g):
                P_min[i] = random.uniform(10, 1000)
                P_max[i] = random.uniform(P_min[i], 1000)
                A[i] = random.uniform(0, 10)
                B[i] = random.uniform(0, 100)
                C[i] = random.uniform(0, 1000)

                P_tot_high += P_max[i]
                P_tot_low += P_min[i]

            # print space separated values
            file.write(" ".join(list(map(str,P_min))) + "\n")
            file.write(" ".join(list(map(str,P_max))) + "\n")
            file.write(" ".join(list(map(str,A))) + "\n")
            file.write(" ".join(list(map(str,B))) + "\n")
            file.write(" ".join(list(map(str,C))) + "\n")

            # load and loss sum to a value in the bounds between the min possible power the generators suply
            # and the maximum power the generators supply
            P_tot = random.uniform(P_tot_low, P_tot_high)
            P_load = random.uniform(0, P_tot)
            P_loss = P_tot - P_load

            file.write(str(P_load) + "\n")
            file.write(str(P_loss) + "\n")