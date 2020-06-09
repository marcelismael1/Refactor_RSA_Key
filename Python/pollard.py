# Pollard P-1 Method
# https://mathworld.wolfram.com/Pollardp-1FactorizationMethod.html
# https://www.mersenne.org/various/math.php

from math import gcd

def solve_pollard(n):
    print("\nRefactoring N with Pollard P-1 Method:\n")
    a = 2
    B = 100000
    for i in range(2,B):
        a = pow(a,i,n)
        p = gcd(a-1,n)
        if p>1:
            if n%p ==0:
                q = n//p
                result = {}
                result['p'] = p
                result['q'] = q
                print("\nPollar P-1 Method finished, N was refactored\n")
                return result
                break              
    print("\nPollar P-1 Method finished, Failed\n")
    return False


if __name__ == "__main__":

   n = 1035896947 *3500688283
   print('This is to test Pollard P-1 Algorithm')
   print( 'n = ',n)
   pq = solve_pollard(n)
   print ("p = ", pq['p'])
   print ("q = ", pq['q'])