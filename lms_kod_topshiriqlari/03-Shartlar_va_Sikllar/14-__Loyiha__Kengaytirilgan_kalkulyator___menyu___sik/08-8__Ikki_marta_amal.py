while True:
    n = input().strip()
    if n == "0":
        print("Exit")
        break
    a, b = map(int, n.split())
    t = int(input())
    
    if t == 1: print(a + b)
    if t == 2: print(a - b)
    if t == 3: print(a * b)
    if t == 4: print(a / b)