def calculator():
    # Get the user's input for the first number
    num1 = float(input("Enter the first number: "))
 
    # Get the user's input for the second number
    num2 = float(input("Enter the second number: "))
 
    # Get the user's input for the operator
    operator = input("Enter the operator (+, -, *, /): ")
 
    # Perform the operation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = "Invalid operator"
 
    # Print the result
    print(result)

calculator()