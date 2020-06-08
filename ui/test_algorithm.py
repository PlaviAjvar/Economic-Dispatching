import algorithm

if __name__ == "__main__":
    P_min = [100, 90, 30]
    P_max = [550, 450, 230]
    p_load = 980
    p_loss = 20
    A = [0.001632, 0.00241, 0.00514]
    B = [6.852, 8.05, 8.82]
    C = [405, 293, 81]

    (P, iter_count, total_price, total_power, total_power_loss) = algorithm.run_algorithm(
        P_min, P_max, p_load, p_loss, A, B, C
    )

    print("P =", P)
    print("Iterations:", iter_count)
    print("Total cost =", total_price)
    print("Total power =", total_power)
    print("Power loss =", total_power_loss)