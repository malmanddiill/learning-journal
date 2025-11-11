# Strings and methods
s = "  hello, Majed!  "
print(s.strip())
print(s.lower())
print(s.upper())
print(s.replace("Majed", "Friend"))
print("Majed" in s)
print(",".join(["a", "b", "c"]))
print("split ->", "a,b,c".split(","))

# f-strings
name = "Majed"
age = 18
print(f"{name} is {age} years old")

# CSV write/read
import csv
rows = [
    ["name", "age", "city"],
    ["Majed", 18, "Riyadh"],
    ["Sara", 22, "Jeddah"],
]

with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
print("CSV rows:", data)

# JSON write/read
import json

profile = {
    "name": "Majed",
    "skills": ["python", "sql", "html"],
    "active": True,
    "score": 95.5,
}

with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(profile, f, ensure_ascii=False, indent=2)

with open("profile.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print("JSON loaded:", loaded)
