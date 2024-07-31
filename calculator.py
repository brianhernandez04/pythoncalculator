# Addition
def add(n1, n2):
    return n1 + n2
# Subtraction
def subtract(n1, n2):
    return n1 - n2
# Multiplication
def multiply(n1, n2):
    return n1 * n2
# Division
def divide(n1, n2):
    return n1 / n2

#  Dictionary containing Operators
operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# Recursion Function/While Loop nested withing
def calculator():
    continuation = True
    num1 = float(input("Input a number: "))

    while continuation:
        # Prints each operator
        for symbol in operation:
            print(symbol)

        operator_choice = input("Select an operator: ")
        operator = operation[operator_choice]

        num2 = float(input("Input the second number: "))

        # Operator is the function of the operations icon that the user chose from "operator_choice"
        first_ans = operator(num1, num2)
        print(f"{num1} {operator_choice} {num2} = {first_ans}")

        option = input(f"Type 'y' to continue calculating with {first_ans}, 'n' to start a new calculation, or 'e' to escape the application: ")

        if option == "y":
            # The first answer is now "num1", therfore continues the calculation with the first answer
            num1 = first_ans
        elif option == "e":
            print("Thank you & happy calculations.... Goodbye!")
            continuation = False
        else:
            continuation = False
            calculator()

calculator()


