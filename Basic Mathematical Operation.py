a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum_ = a + b
diff = a - b
prod = a * b

print("Addition:", sum_)
print("Subtraction:", diff)
print("Multiplication:", prod)

div = a / b if b != 0 else "Undefined (cannot divide by zero)"
print("Division:", div)
