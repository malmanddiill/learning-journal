def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

def km_to_mi(km):
    return km * 0.621371

def mi_to_km(mi):
    return mi / 0.621371

def get_float(prompt):
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print("Please enter a number (e.g., 12 or 12.5).")

def main():
    print("Unit Converter")
    print("1) Celsius → Fahrenheit")
    print("2) Fahrenheit → Celsius")
    print("3) Kilometers → Miles")
    print("4) Miles → Kilometers")
    choice = input("Choose 1-4: ").strip()

    if choice == "1":
        c = get_float("Celsius: ")
        print("Fahrenheit:", round(c_to_f(c), 2))
    elif choice == "2":
        f = get_float("Fahrenheit: ")
        print("Celsius:", round(f_to_c(f), 2))
    elif choice == "3":
        km = get_float("Kilometers: ")
        print("Miles:", round(km_to_mi(km), 3))
    elif choice == "4":
        mi = get_float("Miles: ")
        print("Kilometers:", round(mi_to_km(mi), 3))
    else:
        print("Please run again and choose 1-4.")

if __name__ == "__main__":
    main()