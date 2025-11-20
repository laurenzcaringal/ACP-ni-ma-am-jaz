import math

s = input("Type something: ")
n = float(input("Type a number: "))

print("Upper:", s.upper())
print("Lower:", s.lower())
print("Length of string:", len(s))
print("Reversed string:", s[::-1])

print("Square root of number:", math.sqrt(n))
print("Number squared:", n**2)
print("Ceil value:", math.ceil(n))
print("Floor value:", math.floor(n))
print("Absolute:", abs(n))
