# 1) Sign checker
x = float(input("Enter a number: "))
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

# 2) Even/odd
n = int(input("Enter an integer: "))
print("even" if n % 2 == 0 else "odd")

# 3) Simple grade
score = float(input("Score 0-100: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 4) Mini calculator
a = float(input("a: "))
op = input("op (+ - * /): ").strip()
b = float(input("b: "))
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b if b != 0 else "Infinity")
else:
    print("Unknown operator")



n = int(input("n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("sum:", total)



