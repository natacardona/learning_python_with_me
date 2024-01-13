def sum(num1,num2):
    # Check if the variable is an integer
    if isinstance(num1, int) and isinstance(num2,int):
        return num1+num2
    else:
        print("This method not allow strings.")
    

#Testing sum
seven = sum(1,6)
test_string = sum("1", "6")
print(seven)
print(test_string)