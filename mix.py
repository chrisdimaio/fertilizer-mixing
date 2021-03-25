def calculate(n, p, k, fn, fp, fk, coverage, area):
    p_coverage = coverage * (p/n)
    k_coverage = coverage * (k/n)

    n_concentration = fn/100
    p_concentration = fp/100
    k_concentration = fk/100

    # coverage adjusted for concentration.
    n_adjusted = coverage/n_concentration
    p_adjusted = p_coverage/p_concentration
    k_adjusted = k_coverage/k_concentration

    scalar = area/1000

    n_scaled = n_adjusted * scalar
    p_scaled = p_adjusted * scalar
    k_scaled = k_adjusted * scalar

    return (n_scaled, p_scaled, k_scaled)
