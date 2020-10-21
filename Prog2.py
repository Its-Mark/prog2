# Mark Garcia
# Programming Assignment 2
# CECS 229-05
# Due:

from math import sqrt
from random import randint

def gcd(a, b):
    if b == 0:
        return a
    else:
        gcd(b, a % b)


# 1. Generate valid keys (e, n) for the RSA cryptosystem.
def rsa(num):
    divsList = findDivs(num)
    p = 0
    q = 0
    #get two biggest primes in the number
    for i in range(len(divsList)):
        if divsList[i] > p:
            q = p
            p = divsList[i]
    n = p * q
    e = 0
    for e in range(num):
        if gcd(e, (p-1) * (q-1)) == 1:
            break
    print("key e = " + str(e))
    print("key n = " + str(n))


# 2. Use the sieve of Eratosthenes to find all primes less than 10,000.
def sieveOfErato(num):
    # algorithm Sieve of Eratosthenes is
    # input: an integer n > 1.
    # output: all prime numbers from 2 through n.
    #
    # let A be an array of Boolean values, indexed by integers 2 to n,
    # initially all set to true.
    #
    # for i = 2, 3, 4, ..., not exceeding √n do
    # if A[i] is true
    #     for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
    #     A[j] := false
    #
    # return all i such that A[i] is true.

    primes = [True for i in range(num + 1)]
    p = 2
    while p <= sqrt(num):
        if primes[p] == True:
            for i in range(2 * p, num + 1, p):
                primes[i] = False
        p += 1

    primes[0] = False
    primes[1] = False

    for x in range(num + 1):
        if primes[x]:
            print(x)


# 3. Find all of the positive divisors of a positive integer from its prime factorization.
def findDivs(num):
    divs = []
    while num % 2 == 0:
        divs.append(2)
        num = num / 2

    for i in range(3, int(sqrt(num)) + 1, 2):
        while num % i == 0:
            divs.append(i)
            num = num / i

    if num > 2:
        divs.append(num)

    return divs


def main():
    x = randint(100, 10000)
    print("All positive divisors from prime factorization of: " + str(x))
    print(findDivs(x))

    print("All prime factors that are <= " + str(x))
    sieveOfErato(x)

    print("Running RSA Encryption Algorithm....")
    rsa(x)

main()
