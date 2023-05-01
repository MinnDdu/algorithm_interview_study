def binomialCoeff_DP1D(n, k):
    """
    :type n: integer
    :type k: integer
    :rtype: integer
    """
    ### BEGIN SOLUTION
    c = []
    for i in range(k + 1):
        c.append(0)
    c[0] = 1

    for i in range(n + 1):
        for j in range(min(i, k), 0, -1):
            if j == 0 or j == i:
                c[j] = 1
            else:
                c[j] = c[j] + c[j - 1]
    return c[k]

print(binomialCoeff_DP1D(4, 2))