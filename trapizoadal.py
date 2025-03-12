import numpy as np
def trapezoidal_rule(f,a,b,n):
    h = (b - a )/n
    x = np.linspace(a,b,n+1)
    y = f(x)
    
    integral = (h/2)*(y[0]+2*sum(y[1:n])+y[n])
    return integral

def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5


a=0
b=0.8
n=2

result = trapezoidal_rule(f,a,b,n)
print(f"Approximate integral: {result}")