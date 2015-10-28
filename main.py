#! /usr/bin/python

import primes

sage = primes.PrimeSage('primes.pickle')


def verboseTestPrime(t):
    print "%d is%s prime." % (t, ('' if sage.is_prime(t) else " not"))

if (__name__ == "__main__"):
    #verboseTestPrime(2)
    #verboseTestPrime(3)
    #verboseTestPrime(20)
    #verboseTestPrime(7)
    verboseTestPrime(101)
