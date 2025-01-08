def bisection_method(func, a, b, tol=1e-6):
   
    if func(a) * func(b) >= 0:
        print("Bisection method fails. The function must have opposite signs at a and b.")
        return None

    while (b - a) / 2.0 > tol:
        c= (a + b) / 2.0
        if func(c) == 0:  
            return c
        elif func(a) * func(c) < 0:  
            b = c
        else: 
            a = c

    return (a + b) / 2.0


if __name__ == "__main__":
   
    equation_input = input("Enter the equation in terms of x : ")

    def func(x):
        return eval(equation_input)

    a = float(input("Enter the lower bound of the interval (a): "))
    b = float(input("Enter the upper bound of the interval (b): "))

   
    tolerance = 1e-6


    root = bisection_method(func, a, b, tolerance)
    if root is not None:
        print(f"The root of the equation is approximately: {root}")
