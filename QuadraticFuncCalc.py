
import math

def begin():
    print("PLEASE INSERT COEFFICIANTS")
    print("A > ", end="")
    A = float(input())
    print("B > ", end="")
    B = float(input())
    print("C > ", end="")
    C = float(input())
    quadr(A,B,C)


def quadr(A,B,C):
    discr = B*B-4*A*C
    if discr <0:
        print("NO ROOTS")
    elif discr == 0:
        print("ONE ROOT - VERTEX " +str(-B/2*A))
    else:
        root1 = (-B + math.sqrt(discr))/2*A
        root2 = (-B - math.sqrt(discr))/2*A
        print("two roots " +str(round(root1, 4)) + " and " +str(round(root2, 4)))

begin()
