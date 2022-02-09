def derivative (f,h):
    return lambda x: (f(x+h) -f (x)) / h

def square(x):
    return x**2

def kthDerivative(f, h , k):
    if k == 1:
        return derivative(f,h)
    else:
        return derivative(kthDerivative(f,h,k-1), h)
    
def quartic(x):
    return x**4


g = kthDerivative(quartic, 0.0001, 3)
print(g(10))