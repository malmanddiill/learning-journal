# Basic try/except
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both must be numbers"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "x"))

# File handling with try/except
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"File '{filename}' not found"
    except Exception as e:
        return f"Error: {e}"

print(read_file_safe("people.csv"))
print(read_file_safe("nonexistent.txt"))

# Simple tests
def test_is_even():
    assert 4 % 2 == 0
    assert 5 % 2 != 0
    print("✓ test_is_even passed")

def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) == "Cannot divide by zero"
    print("✓ test_safe_divide passed")

def test_read_file():
    result = read_file_safe("people.csv")
    assert "name" in result or "Majed" in result
    print("✓ test_read_file passed")

if __name__ == "__main__":
    test_is_even()
    test_safe_divide()
    test_read_file()
    print("\nAll 3 tests passed!")
