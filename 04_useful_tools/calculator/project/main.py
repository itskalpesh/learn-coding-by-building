print("Enter first number:")
num1 = float(input())

print("Enter second number:")
num2 = float(input())

print("Choose operation (+, -, *, /):")
operation = input()

if operation == "+":
    print("Result:", num1 + num2)

elif operation == "-":
    print("Result:", num1 - num2)

elif operation == "*":
    print("Result:", num1 * num2)

elif operation == "/":
    print("Result:", num1 / num2)

else:
    print("Invalid operation.")
