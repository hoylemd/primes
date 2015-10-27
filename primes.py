#!/usr/bin/python
primes = [2]
known_primes = 1


def test_divisible(numerator, divisor):
    return (numerator % divisor) == 0


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


class PrimeSage(object):
    def __init__(self, data_path):
        self.data_path = data_path

        self.primes = [2]

    def is_prime(self, sample):
        greatest = self.primes[-1]
        # if the test number is higher than the highest known prime,
        # calculate primes until we have enough
        if sample > greatest:
            next_candidate = greatest
            while sample > greatest:
                # start calculating primes until we reach this one or go higher
                next_candidate += 1
                if not self.has_prime_divisor(next_candidate):
                    self.primes.append(next_candidate)
                    greatest = next_candidate
            if sample == greatest:
                return True
            return False
        return binary_search(sample, self.primes)

    def has_prime_divisor(self, sample):
        if sample > (self.primes[-1] * 2):
            raise Exception("going way too far!")

        left = 0
        right = len(self.primes) - 1

        while left <= right:
            if test_divisible(sample, self.primes[left]):
                return True
            left += 1

            if test_divisible(sample, self.primes[right]):
                return True
            right -= 1

        return False

sage = PrimeSage('primes.pickle')


def verboseTestPrime(t):
    print "%d is%s prime." % (t, ('' if sage.is_prime(t) else " not"))
