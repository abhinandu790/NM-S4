def f(x):
    return x**3 + 2*x**2 - 5*x + 7

def forward_difference(x, h):
    return (f(x + h) - f(x)) / h

x = 2
h = 0.1
first_derivative = forward_difference(x, h)

print(f"First derivative of x**3 + 2*x**2 - 5*x + 7 :{first_derivative}")
