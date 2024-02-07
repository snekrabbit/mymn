import math

def begin():
    print("PLEASE INSERT KNOWN TRIANGLE PARAMETERS (MINIMUM 3)")
    print("enter \"0\" for unknown variables")
    print("a > ", end="")
    a = float(input())
    print("b > ", end="")
    b = float(input())
    print("c > ", end="")
    c = float(input())
    print("A > ", end="")
    A = float(input())
    print("B > ", end="")
    B = float(input())
    print("C > ", end="")
    C = float(input())
   # print(sumang(A,B))
    print("a=",a," b=",b, " C=",C)
    if C == 0:
        print(lcosr(a,b,c))
    else:
        print(lcos(a,b,C))


def sumang(A,B):
    return(180 - A - B)

def lcos(s1,s2,A):
    return(math.sqrt(s1**2 + s2**2 - 2 * s1 * s2 * math.cos(A*math.pi/180)))

def lcosr(s1,s2,s3):
    cos12=(s1**2 + s2**2 - s3**2)/(2 * s1 * s2)
    print(cos12)
    A12=math.acos(cos12)
    print(math.degrees(A12))
    return(math.degrees(math.acos((s1**2 + s2**2 - s3**2)/(2 * s1 * s2))))
    

    
    
begin()