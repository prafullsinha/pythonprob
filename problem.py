def egg(n, k):
    if k == 1 or k == 0:
        return k
    if n == 1:
        return k
    m = 1000000
    for x in range(1, k + 1):
        val = max(egg(n - 1, x - 1),
                  egg(n, k - x))
        if val < m:
            m = val
    return m + 1
