a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"Addition of two numbers: {a + b}")
print(f"Subtraction of two numbers: {a - b}")
print(f"Multiplication of two numbers: {a * b}")

if b != 0:
    print(f"Division of two numbers: {a / b}")
else:
    print("Division of two numbers: Error (cannot divide by zero)")
