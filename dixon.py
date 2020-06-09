# Dixon Factorization Method
#https://mathworld.wolfram.com/DixonsFactorizationMethod.html

import commonfucntions as common
from math import sqrt
from random import randint

def factorize_B_smooth (n ,b):
    '''
    This function will take a number n and list of primes
    and it wull refactor n to and return a dict
    '''
    N = n
    result = dict(list(zip(b,[0 for _ in range(len(b))]))) 
    i = 0
    while (N!=1) and not(common.check_prime(N) and (N not in result.keys())):
        for k in result:
            if N%k == 0:
                N -=  (N - (N/k))
                result[k] +=1
            elif i == 0 and len(set(result.values())) != len(b):
                N = 1
                break           
        i+=1
    return result   

def solve_dixon(n):
    # Set B value 
    print("\nRefactoring N with Dixon Method:\n")
    B = common.gen_prime_factors(7)
    first_num = int(sqrt(n))
    factored_results = []
    res = []
    while True:
        i = randint(first_num , n+1)
        if len(res) !=2:
            factorized = factorize_B_smooth((i**2)%n,B)
            if 0 not in set(factorized.values()):
                res.append(i)
                factored_results.append(factorized)
        else:
            break
    result = {}
    result['p'] = res[0]
    result['q'] = res[1]
    print("\nDixon Method finished, N was refactored\n")
    return result

if __name__ == "__main__":

   n = 271*139
   print('This is to test Dixon Algorithm')
   print( 'n = ',n)
   pq = solve_dixon(n)
   print ("p = ", pq['p'])
   print ("q = ", pq['q'])
    