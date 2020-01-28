import random


def prime_test(N, k):
    # This is the main function connected to the Test button. You don't need to touch it.
    return run_fermat(N,k), run_miller_rabin(N,k)


def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, math.floor(y/2), N)
    if y % 2 == 0:
        return (z**2) % N
    else:
        return (x * z**2) % N


def fprobability(k):
    # ACCOUNT FOR REPEAT TESTS???????????????????
    return 1 - 0.5**k * k


def mprobability(k):
    return 1 - 0.75**k * k


def run_fermat(N,k):
    randomList = random.sample(range(2, N-2), k)
    for a in randomList:
        # a = random.randint(2, N-2)
        if a**(N-1) % N != 1:
            return 'composite'
    return 'prime'


def run_miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    r = 0
    d = N-1
    while (d % 2 == 0):
        d = d / 2
        r += 1

    randomList = random.sample(range(2, N-2), k)
    for a in randomList:
        x = a**d % n
        if x == 1 or x == N - 1:
            continue
        for i in range(r-1):
            x = x**2 % N
            if x == N - 1:
                continue
        return 'composite'
    return 'prime'
    # To generate random values for a, you will most likely want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    # return 'composite'
