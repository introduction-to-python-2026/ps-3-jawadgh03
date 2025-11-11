def approximate_pi(n_terms):
    result = 0
    for i in range(n):
        result += ((-1) ** i) / (2 * i + 1)
    return 4 * result
