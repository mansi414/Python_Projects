from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What is the first number?: "))

    while should_continue:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("pick an operation: ")
        num2 = float(input("what is the second number"))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            "Type 'y to continue calculating from previous step or type 'N' to start a new calculation").lower()

        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()


calculator()
