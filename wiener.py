# Wiener attack
# http://www.hit.bme.hu/~buttyan/Wiener/WienersAttack.pdf

import commonfucntions as common


# Solve Quadratic Equasion
def solve_quadratic_equation(n,phi):
    '''
    solve 
    a*x^2+b*x + c
    and check if roots are n factors
    '''
    a = 1
    b = n - phi +1
    c = n  

    d = (b**2) - (4*a*c)

    s1 = (-b-common.isqrt(abs(d)))//(2*a)
    s2 = (-b+common.isqrt(abs(d)))//(2*a)
    if s1*s2 == n:
        return (abs(s1),abs(s2))
    else:
        return False
        
# Start Wiener Algo       
def solve_wiener(n,e):
    print("\nRefactoring N with Wiener Method:\n")
    # step 1: get e/n convergents
    for i in common.convergents_from_contfrac(common.rational_to_contfrac(e,n)):
        # step 2: check if d not trivial
        if i[1] <2 or i[1]%2==0:
            pass
        else:
            k = i[0]
            d = i[1]

            # Step 3: check if phi is whole value
            if (e*d-1)%k == 0:
                phi =  (e*d-1)//k
                # step4: solve the equasion x^2-(n-phi+1)*x + n and check if the root are n factors.
                pq =  solve_quadratic_equation(n,phi)
                if pq:
                    result = {}
                    result['p'] = pq[0]
                    result['q'] = pq[1]
                    print("\nWiener Method finished, N was refactored\n")
                    return result
                    break
    print("\nWiener Method finished, Failed\n")
    return False
    

if __name__ == "__main__":
    e = 468063471180295465090304528000264421835883255712360150238503461484286356674747
    n = 849904525105248028839166367198578395922976687042693061162002617712237437263151
    print('This is to test Wiener Algorithm')
    print( 'n = ',n)
    print( 'e = ',e)
    pq = solve_wiener(n,e)
    print ("p = ", pq['p'])
    print ("q = ", pq['q'])
