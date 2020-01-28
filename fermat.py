import random
import math


def prime_test(N, k):
    return run_fermat(N,k), run_miller_rabin(N,k)


def mod_exp(x, y, N): # Time complexity: O(log(y)) Space complexity: O(1)
    if y == 0:
        return 1
    z = mod_exp(x, math.floor(y/2), N)
    if y % 2 == 0:
        return (z**2) % N
    else:
        return (x * z**2) % N


def fprobability(k): # Time complexity: O(1) Space complexity: O(1)                     # time complexity????
    return 1 - 0.5**k * k


def mprobability(k): # Time complexity: O(1) Space complexity: O(1)
    return 1 - 0.75**k * k


def run_fermat(N,k): # Time complexity: O(k+log(N-1)) Space complexity: O(k)            # Check
    # create a random list of numbers to test primality
    randomList = random.sample(range(2, N-2), k)

    # test the primality using Fermat's Little Theorem
    for a in randomList:
        if mod_exp(a, N-1, N) != 1:
            return 'composite'
    return 'prime'


def run_miller_rabin(N,k): # Time complexity: O(?????????????) Space complexity: O(k)
    # factor out powers of 2 from N-1
    r = 0
    d = N-1
    while (d % 2 == 0):
        d = d / 2
        r += 1

    # create a random list of numbers to test primality
    randomList = random.sample(range(2, N-2), k)

    # test the primality using the Miller-Rabin primality test
    for a in randomList:                                                                # O(k)
        x = mod_exp(a, d, N)
        if x == 1 or x == N - 1:
            continue
        return_composite = True
        for i in range(r-1):                                                            # worst case, huge??? best case, doesn't even run
            x = mod_exp(x, 2, N)                                                        # O(log(N-1))
            if x == N - 1:
                return_composite = False
                continue
        if return_composite:
            return 'composite'
    return 'prime'
