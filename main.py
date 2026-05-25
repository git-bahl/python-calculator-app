# Get the user's selected operation

def user_operation():
    try:
        operation = int(input("what operation would you like to perform? Choose from below options:\n"
            " 1. addition\n"
            " 2. subtraction\n"
            " 3. multiplication\n"
            " 4. division\n"
            " 5. exit \n"
            "Enter your choice: "))
    except ValueError:
        print("Invalid Choice; Please only enter a number.")
        return None
    return operation

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def main():    

    while True:
        operation = user_operation()
        if operation is None:
            continue

        if operation == 5:
            print("Goodbye!!")
            break
        elif operation in (1, 2, 3, 4):
            # Get two numbers from the user
            try:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid number entered")
                continue

            # Perform the selected calculation
            if operation == 1:
                result = addition(x, y)
            elif operation == 2:
                result = subtraction(x, y)
            elif operation == 3:
                result = multiplication(x, y)
            elif operation == 4:
                result = division(x, y)
            print("Result: ", result)
        else:
            print("Wrong entry. try again!!")
    

# Run the calculator app
if __name__ == "__main__":
    main()


