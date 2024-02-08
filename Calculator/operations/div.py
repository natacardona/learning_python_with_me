from numbers import Real

def div(num1, num2):
    # Check if both inputs are numbers
    if isinstance(num1, Real) and isinstance(num2, Real):
        try:
            return num1 / num2
        except ZeroDivisionError:
            raise Exception("You can't divide any number by zero.") 