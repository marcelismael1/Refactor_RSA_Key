from wiener import solve_wiener
from pollard import solve_pollard
from dixon import solve_dixon

if __name__ == "__main__":
    while True:
        try:
            n = int(input(" Enter N to refactor:"))
            e = int(input(" Enter e Exponent:"))
            break
        except:
            pass

    # Check if e is big run wiener (d must be larg)
    if e > (n//8):
        pq = solve_wiener(n,e)
        if pq:
            print ("p = ", pq['p'])
            print ("q = ", pq['q'])
        else:
            pq = solve_pollard(n)
            if pq:
                print ("p = ", pq['p'])
                print ("q = ", pq['q'])
            else:
                pq = solve_dixon(n)
                if pq:
                    print ("p = ", pq['p'])
                    print ("q = ", pq['q'])
    
    # Case e is small
    else:
        pq = solve_pollard(n)
        if pq:
            print ("p = ", pq['p'])
            print ("q = ", pq['q'])
        else:
            pq = solve_dixon(n)
            if pq:
                print ("p = ", pq['p'])
                print ("q = ", pq['q'])