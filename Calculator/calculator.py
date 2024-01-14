def sum(num1,num2):
    # Check if the input values are numbers
    if (isinstance(num1, int) and isinstance(num2,int)) or (isinstance(num1, float) and isinstance(num2,float)) or (isinstance(num1, int) and isinstance(num2,float)) or (isinstance(num1, float) and isinstance(num2,int)) :
        return num1+num2
    else:
        print("This method not allow strings.")
    

#Test cases
seven = sum(1,6)
test_string = sum("1", "6")
test_float = sum(1720,232)
test_float_and_number = sum(1, 2.3)

