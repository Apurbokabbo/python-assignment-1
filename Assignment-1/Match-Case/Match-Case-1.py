def calculator(operator, a, b):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case '^':
            return a ** b
        case _:
            return "Invalid Operator"


print("Sum:",calculator('+', 47, 33))
print("Sub:",calculator('-', 47, 33))
print("Mul:",calculator('*', 5, 10))
print("Div:",calculator('/', 500, 10))
print("Sqr:",calculator('^', 5, 3))