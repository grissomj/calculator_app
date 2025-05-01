import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y
def sqrt(x): return math.sqrt(x)
def exponent(x, y): return x ** y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to the CLI Calculator")
    print("Available operations: add, subtract, multiply, divide, sqrt, exponent")
    
    op = input("Enter operation: ").lower().strip()

    if op == "sqrt":
        num = get_number("Enter number: ")
        print("Result:", sqrt(num))
    else:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        if op == "add":
            print("Result:", add(num1, num2))
        elif op == "subtract":
            print("Result:", subtract(num1, num2))
        elif op == "multiply":
            print("Result:", multiply(num1, num2))
        elif op == "divide":
            print("Result:", divide(num1, num2))
        elif op == "exponent":
            print("Result:", exponent(num1, num2))
        else:
            print("Invalid operation.")

if __name__ == "__main__":
    main()
