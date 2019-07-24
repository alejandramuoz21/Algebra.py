import numpy as np
def GauusBasico1(a, b):
    n = len(b)
    I = np.identity(n)
    c = np.concatenate([a, b], axis=1)
    for e in range(n):
        t = c[e, e]
        for j in range(e, n + 1):
            c[e, j] = c[e, j] / t
        for i in range(n):
            if i != e:
                t = c[i, e]
                for j in range(e, n + 1):
                    c[i, j] = c[i, j] - t * c[e, j]
    x = c[:, n]

    for i in range(n - 1):
        s = 0
        for j in range(i + 1):
            s = s + c[i, j] * x[j]
    x = c[:, n + 1, -s]
    return x