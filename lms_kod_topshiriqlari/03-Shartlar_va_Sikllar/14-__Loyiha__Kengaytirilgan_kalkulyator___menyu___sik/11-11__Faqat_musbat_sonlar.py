n = input().strip()
a, b = map(int, n.split())
t = int(input())

if a < 0 or b < 0:
    print("Invalid")
else:
    amallar = {1: a + b, 2: a - b, 3: a * b, 4: a / b, 5: a % b, 6: a ** b}
    print(amallar[t])