import random
import math


def prime_test(N, k):
    return run_fermat(N,k), run_miller_rabin(N,k)


def mod_exp(x, y, N): # Time complexity: O(n^3) Space complexity: O(n)
    if y == 0:  # O(1)
        return 1
    z = mod_exp(x, math.floor(y/2), N)  # y is an n-bit number, so there will be n recursive calls
    if y % 2 == 0:
        return (z**2) % N # O(n^2) bc of multiplication
    else:
        return (x * z**2) % N # size of this result is n bits (time). O(n^2) bc of multiplication


def fprobability(k): # Time complexity: O(n^2) bc of multiplication of 2 n bit numbers Space complexity: O(n)
    return 1 - 0.5**k


def mprobability(k): # Time complexity: O(n^2) bc of multiplication of 2 n bit numbers Space complexity: O(n)
    return 1 - 0.25**k


def run_fermat(N,k): # Time complexity: O(n^3) Space complexity: O(k)
    # create a random list of numbers to test primality
    randomList = random.sample(range(2, N-2), k)    # O(1) independent of input. could be exponentially longer, but we don't know

    # test the primality using Fermat's Little Theorem
    for a in randomList:
        if mod_exp(a, N-1, N) != 1:
            return 'composite'
    return 'prime'


def run_miller_rabin(N,k): # Time complexity: O(n^4) Space complexity: O(n)
    # factor out powers of 2 from N-1 (2^r * d - 1 = N)
    r = 0
    d = N-1
    while (d % 2 == 0):
        d = d / 2
        r += 1

    # create a random list of numbers to test primality
    randomList = random.sample(range(2, N-2), k)

    # test the primality using the Miller-Rabin primality test
    for a in randomList:
        x = mod_exp(a, d, N)        # O(n^3)
        if x == 1 or x == N - 1:
            continue
        return_composite = True
        for i in range(r-1):        # O(n)
            x = mod_exp(x, 2, N)
            if x == N - 1:
                return_composite = False
                continue
        if return_composite:
            return 'composite'
    return 'prime'
