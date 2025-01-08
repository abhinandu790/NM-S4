def bisection_method(func, a, b, tol=1e-6):
    """
    Find a root of a function using the Bisection Method.

    Parameters:
    func : function
        The nonlinear equation to solve (f(x)).
    a : float
        The lower bound of the interval.
    b : float
        The upper bound of the interval.
    tol : float, optional
        The tolerance level for stopping criteria (default is 1e-6).

    Returns:
    float
        The root of the equation within the given tolerance.
    """
    if func(a) * func(b) >= 0:
        print("Bisection method fails. The function must have opposite signs at a and b.")
        return None

    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if func(midpoint) == 0:  # We've found the root
            return midpoint
        elif func(a) * func(midpoint) < 0:  # Root lies in [a, midpoint]
            b = midpoint
        else:  # Root lies in [midpoint, b]
            a = midpoint

    return (a + b) / 2.0


if __name__ == "__main__":
    # Input the equation as a string
    equation_input = input("Enter the equation in terms of x (e.g., x**3 - 4*x - 9): ")

    # Define the function dynamically using eval
    def func(x):
        return eval(equation_input)

    # Input the interval [a, b]
    a = float(input("Enter the lower bound of the interval (a): "))
    b = float(input("Enter the upper bound of the interval (b): "))

    # Fixed tolerance
    tolerance = 1e-6

    # Find the root
    root = bisection_method(func, a, b, tolerance)
    if root is not None:
        print(f"The root of the equation is approximately: {root}")
