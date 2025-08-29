'''
Take two positive integers from the user. Verify if (a+b)^3 = a^3 + b^3 + 3a^2b + 3ab^2.

Calculate the Left hand side (LHS) and the right hand side (RHS) of the equation. Print the (LHS) and the (RHS).

Print VERIFIED in uppercase if they are equal, otherwise print NOT VERIFIED.

'''

if __name__=='__main__':
    a, b=map(int,input().split())
    lhs=(a+b)**3
    rhs=a**3+b**3+3*a**2*b+3*a*b**2
    print(lhs)
    print(rhs)
    if lhs==rhs:
        print("VERIFIED")
    else:
        print("NOT VERIFIED")    