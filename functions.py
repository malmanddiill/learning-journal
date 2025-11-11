def greet(name: str) -> str:
    return f"Hello, {name}!"

def area_circle(r: float) -> float:
    pi = 3.141592653589793
    return pi * r * r

def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == "__main__":
    print(greet("Majed"))
    print("Area:", round(area_circle(3), 2))
    print("Is 4 even?", is_even(4))