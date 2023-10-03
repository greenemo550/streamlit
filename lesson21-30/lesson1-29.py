try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation not in ['+', '-', '*', '/']:
        raise ValueError("Invalid operator")


    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2

    print(f"Result: {result}")

except ValueError as ve:
    if str(ve) == "Invalid operator":
        print("Invalid operator. Please use +, -, *, or /.")
    else:
        print("Please enter a valid number.")
except ZeroDivisionError:
    print("You can't divide by zero!")