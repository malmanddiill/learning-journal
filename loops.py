# 1) Sum 1..n
n = int(input("n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("sum:", total)

# 2) Times table for k
k = int(input("k: "))
for i in range(1, 11):
    print(f"{k} x {i} = {k*i}")

# 3) Guessing game
secret = 7
while True:
    g = int(input("guess 1-10: "))
    if g == secret:
        print("correct!")
        break
    print("try again")