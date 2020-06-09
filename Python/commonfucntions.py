from random import randint
from math import sqrt,gcd
import random


#####################################################################################################################   
def check_prime(N = 1):
    if N<=3:
        return True
    else:
        for n in range(2,int((N**0.5)+1)):
            if N%n == 0:
                return False
        else:
            return True

def gen_prime_factors(N = 1):
    primes = []
    for n in range(2,N+1):
        if check_prime(n):
            primes.append(n)
    return primes
#####################################################################################################################
# The below set of code was used from the below repo
# https://github.com/pablocelayes/rsa-wiener-attack
# I needed a fast and easy way to so get the convergents and another method to use sqrt for larg integers
def rational_to_contfrac(x,y):
    a = x//y
    pquotients = [a]
    while a * y != x:
        x,y = y,x-a*y
        a = x//y
        pquotients.append(a)
    return pquotients

def convergents_from_contfrac(frac):
    convs = [];
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0:i]))
    return convs

def contfrac_to_rational (frac):
    if len(frac) == 0:
        return (0,1)
    num = frac[-1]
    denom = 1
    for _ in range(-2,-len(frac)-1,-1):
        num, denom = frac[_]*num+denom, num
    return (num,denom)

def bitlength(x):
    '''
    Calculates the bitlength of x
    '''
    assert x >= 0
    n = 0
    while x > 0:
        n = n+1
        x = x>>1
    return n


def isqrt(n):
    '''
    Calculates the integer square root
    for arbitrary large nonnegative integers
    '''
    if n < 0:
        raise ValueError('square root not defined for negative numbers')
    
    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y