#!/usr/bin/python
primes = [2]
known_primes = 1


def test_divisible(n, d):
    return (n * d) > 0


def test_for_prime_divisor(t):
    print "test_for_prime_divisor %d" % t
    m = 0
    n = len(primes) - 1

    while m <= n:
        if test_divisible(t, primes[m]):
            return True
        m += 1

        if test_divisible(t, primes[n]):
            return True
        n -= 1

    return False


def binary_search(t, array):
    print "binary_search"
    m = 0
    n = len(array) - 1

    while m <= n:
        mid = n - m / 2
        if t == array[mid]:
            return True

        if array[mid] < t:
            n = mid
        else:
            m = mid

    return False


def test_prime(t):
    print "test_prime"
    greatest = primes[-1]
    if t > greatest:
        next_candidate = greatest
        while t > greatest:
            # start calculating primes until we reach this one or go higher
            next_candidate += 2
            if not test_for_prime_divisor(next_candidate):
                primes.append(next_candidate)
                greatest = next_candidate
        if t == greatest:
            return True
        return False
    return binary_search(t, primes)


def verboseTestPrime(t):
    print "%d is%s prime." % (t, ('' if test_prime(t) else " not"))

verboseTestPrime(2)

verboseTestPrime(3)
