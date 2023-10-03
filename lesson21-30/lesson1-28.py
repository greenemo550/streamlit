try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result is: {result}")
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You can't divide by zero!")

