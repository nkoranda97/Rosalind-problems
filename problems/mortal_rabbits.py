def mortal_rabbits(n, m):
    p = [1, 1]
    for n in range(2, n):
        if n < m:
            p.append(p[n - 1] + p[n - 2])
        elif n == m:
            p.append(p[n - 1] + p[n - 2] - 1)
        else:
            p.append(p[n - 1] + p[n - 2] - p[n - m - 1])
    return p[-1]


print(mortal_rabbits(89, 19))
