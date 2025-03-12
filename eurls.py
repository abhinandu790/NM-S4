import numpy as np

def Euler_method(f,x0,y0,x_final, h):
    x = x0
    y = y0
    
    while x< x_final:
        y = y+h*f(x,y)
        x = x+h
    return y

def f(x, y):
    return x**2 - y

x0 , y0 = 0, 0
x_final = 4
h = 0.4

y_approx = Euler_method(f,x0,y0,x_final, h)
print(f"Approximate value of y({x_final}) = {y_approx}")