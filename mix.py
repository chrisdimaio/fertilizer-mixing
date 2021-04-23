def calculate_concentrations(fn, fp, fk):
    return (fn/100, fp/100, fk/100)


def calculate_coverage(n, p, k, fn, fp, fk, coverage, area):
    p_coverage = coverage * (p/n)
    k_coverage = coverage * (k/n)

    n_concentration, p_concentration, k_concentration = fn/100, fp/100, fk/100

    # coverage adjusted for concentration.
    n_adjusted = coverage/n_concentration
    p_adjusted = p_coverage/p_concentration
    k_adjusted = k_coverage/k_concentration

    scalar = area/1000

    n_scaled = n_adjusted * scalar
    p_scaled = p_adjusted * scalar
    k_scaled = k_adjusted * scalar

    return (n_scaled, p_scaled, k_scaled)


def calculate_weight(n, p, k, fn, fp, fk, weight):
    # 100 parts for each of the parts n p k.
    total_parts = n + p + k

    n_percent = n / total_parts
    p_percent = p / total_parts
    k_percent = k / total_parts

    n_weight = weight * n_percent
    p_weight = weight * p_percent
    k_weight = weight * k_percent

    total = n_weight + p_weight + k_weight

    return weight * n_percent, weight * p_percent, weight * k_percent

# def calculate_weight(n, p, k, fn, fp, fk, weight):
#     # n_coverage = weight / n
#     p_coverage = 1 * (p/n)
#     k_coverage = 1 * (k/n)

#     n_concentration, p_concentration, k_concentration = fn/100, fp/100, fk/100

#     # coverage adjusted for concentration.
#     n_adjusted = 1/fn
#     p_adjusted = 1/fp
#     k_adjusted = 1/fk

#     print(n_adjusted, p_adjusted, k_adjusted)

#     total_adjusted = n_adjusted + p_adjusted + k_adjusted

#     n_percent = n_adjusted / total_adjusted
#     p_percent = p_adjusted / total_adjusted
#     k_percent = k_adjusted / total_adjusted

#     print(n_percent, p_percent, k_percent)

#     return weight * n_percent, weight * p_percent, weight * k_percent
