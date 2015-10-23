#!/usr/bin/python
primes = [2]
known_primes = 1


def test_divisible(numerator, divisor):
    return (numerator % divisor) == 0


def test_for_prime_divisor(t):
    if t > 35:
        raise Exception

    left = 0
    right = len(primes) - 1

    while left <= right:
        if test_divisible(t, primes[left]):
            return True
        left += 1

        if test_divisible(t, primes[right]):
            return True
        right -= 1

    return False


def binary_search(t, array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = ((right - left) / 2) + left
        if t == array[mid]:
            return True

        if array[mid] < t:
            left = mid
        else:
            right = mid

    return False


def test_prime(t):
    greatest = primes[-1]
    # if the test number is higher than the highest known prime,
    # calculate primes until we have enough
    if t > greatest:
        next_candidate = greatest
        while t > greatest:
            # start calculating primes until we reach this one or go higher
            next_candidate += 1
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

verboseTestPrime(20)

verboseTestPrime(7)

# verboseTestPrime(101)
