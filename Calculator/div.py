from numbers import Real

def div(num1, num2):
    # Check if both inputs are numbers
    if isinstance(num1, Real) and isinstance(num2, Real):
        return num1 / num2