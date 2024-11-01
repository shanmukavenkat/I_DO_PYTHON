import sympy

a = int(input())
if sympy.isprime(a):
    print("It is Prime")
else:
    print("It is not a prime")
