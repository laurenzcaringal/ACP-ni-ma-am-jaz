ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Undefined (cannot divide by zero)"
}

while True:
    numbers = input("Enter two numbers separated by space: ").split()
    if len(numbers) != 2:
        print("Please enter exactly two numbers.")
        continue

    try:
        a, b = map(float, numbers)
    except ValueError:
        print("Invalid numbers. Try again.")
        continue

    op = input("Enter operation (+, -, *, /): ").strip()
    if op not in ops:
        print("Invalid operation. Choose from +, -, *, /")
        continue

    print(f"{a} {op} {b} = {ops[op](a, b)}")

    if input("Calculate again? (yes/no): ").strip().lower() != "yes":
        print("Goodbye!")
        break
