import art

print(art.logo)

# TODO #1: Create various functions with outputs that contains the basic aritmetic operations in math
number1 = int(input("Enter Number 1: "))
number2 = int(input("Enter Number 2: "))

# Add
def add(n1,n2):
    return n1 + n2

# Subtract
def subtract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1,n2):
    return n1 * n2

# Divide
def divide(n1,n2):
    return n1 / n2

# TODO #2: Creates a Dictionary that contains the aritmectic symbols as key and function name as pair values

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# TODO #3: Creates a function that holds the entire calculator program

for symbol in operations:
    print(symbol)
    
operation_symbol = input("Pick an operation from the line above: ")

calculator = operations[operation_symbol] # Obtain the function value by the key in the dictionary
answer = calculator(number1,number2)

print(f"{number1} {operation_symbol} {number2} = {answer}")
