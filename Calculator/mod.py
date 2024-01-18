from numbers import Real

def mod(num1, num2):
    # Check if both inputs are numbers
    if isinstance(num1, Real) and isinstance(num2, Real):
        return num1 % num2
    else:
        print("This method only allows numeric values.")