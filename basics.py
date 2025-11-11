name = input("What's your name? ")
print(f"Hello, {name}!")

age = int(input("Age? "))
print(f"Next year you’ll be {age + 1}")

def get_float(prompt):
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print("Please enter a number (e.g., 12 or 12.5).")

a = get_float("First number: ")
b = get_float("Second number: ")
print("Sum:", a + b)