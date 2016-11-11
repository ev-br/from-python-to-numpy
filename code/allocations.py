# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# -----------------------------------------------------------------------------
import numpy as np
import itertools as it


def solution_1():
    # Brute force
    # 14641 (=11*11*11*11) iterations & tests
    Z = []
    for i in range(11):
        for j in range(11):
            for k in range(11):
                for l in range(11):
                    if i+j+k+l == 10:
                        Z.append((i,j,k,l))
    return Z


def solution_2():
    # Itertools
    # 14641 (=11*11*11*11) iterations & tests
    return [(i,j,k,l)
            for i,j,k,l in it.product(range(11),repeat=4) if i+j+k+l == 10]


def solution_3():
    # Intricated iterations
    # 486 iterations, no test
    return [(a, b, c, (10 - a - b - c))
            for a in range(11) for b in range(11 - a) for c in range(11 - a - b)]

def solution_3_bis():
    # Iterator using intricated iterations
    # 486 iterations, no test
    return ((a, b, c, (10 - a - b - c))
            for a in range(11) for b in range(11 - a) for c in range(11 - a - b))


def solution_4():
    # Numpy indices
    # No iterations, 1331 (= 11*11*11) tests
    X123 = np.indices((11,11,11)).reshape(3,11*11*11)
    X4 = 10 - X123.sum(axis=0)
    return np.vstack((X123, X4)).T[X4 > -1]


if __name__ == '__main__':
    from tools import print_timeit

    print_timeit("solution_1()", globals())
    print_timeit("solution_2()", globals())
    print_timeit("solution_3()", globals())
    print_timeit("solution_4()", globals())
    print()
    print_timeit("solution_3_bis()", globals())
