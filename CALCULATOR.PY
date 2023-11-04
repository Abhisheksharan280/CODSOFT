a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    if b == 0:
        result = "Cannot divide by zero"
    else:
        result = a / b
else:
    result = "Invalid operator"

print(f"Result: {result}")
