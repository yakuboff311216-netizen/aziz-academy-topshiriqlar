a, b = map(int, input().split())
t = int(input())

if a < 0 or b < 0: print("Invalid")
elif b == 0 and t in [4, 5]: print("Error")
else: print([0, a + b, a - b, a * b, a / b, a % b, a ** b][t] )