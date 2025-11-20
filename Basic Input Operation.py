import os, math, statistics

print("Welcome to customer info")
name = input("Enter your name: ") or "N/A"
address = input("Enter your address: ") or "N/A"
phone = input("Enter your phone number: ") or "N/A"
email = input("Enter your email: ") or "N/A"
sex = input("Enter your gender: ") or "N/A"
age = input("Enter your age: ") or "N/A"
srCode = input("Enter your student code: ") or "N/A"

if isinstance(age, str) and age.isdigit():
    age = int(age)

os.system('cls' if os.name == 'nt' else 'clear')

print("\nWelcome to the Math Quiz!")
score = 0

questions = [
    ("What is the square root of 144?", lambda: math.sqrt(144), float),
    ("What is 20 add 30?", lambda: 20 + 30, int),
    ("What is 15 multiply by 3?", lambda: 15 * 3, int),
    ("What is 20 divide by 4?", lambda: 20 / 4, float),
    ("What is 10 minus 4?", lambda: 10 - 4, int),
    ("What is 2 to the power of 3?", lambda: 2 ** 3, int),
    ("What is percentage of 50 out of 200?", lambda: (50 / 200) * 100, float),
    ("What is the value of pi (up to 2 decimal places)?", lambda: round(math.pi, 2), float),
    ("What is the factorial of 5?", lambda: math.factorial(5), int),
    ("What is Median of the following numbers: 3, 1, 4, 2, 5?", lambda: statistics.median([3,1,4,2,5]), float),
]

for i, (prompt, correct_fn, cast) in enumerate(questions, 1):
    try:
        ans = cast(input(f"Question {i}: {prompt}\nYour answer: "))
    except:
        print("Invalid input — counted as incorrect.")
        ans = object()
    correct = correct_fn()
    if ans == correct:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {correct}")

print(f"\n Your total score is: {score} out of {len(questions)}")

if score >= 8:
    print("\nVery good ")
elif 5 <= score < 8:
    print("\nGood")
elif 3 <= score < 5:
    print("\nFair!")
else:
    print("\nBetter luck next time!")
