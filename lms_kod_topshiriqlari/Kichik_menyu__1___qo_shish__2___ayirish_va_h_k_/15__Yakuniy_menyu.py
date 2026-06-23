while True:
    k = input().split()
    if k[0] == '0': print("Exit"); break
    
    a, b = float(k[0]), float(k[1])
    amal = input()
    
    if amal == '1': print(int(a + b))
    elif amal == '2': print(int(a - b))
    elif amal == '3': print(int(a * b))
    elif amal == '4': print(a / b)
    elif amal == '0': print("Exit"); break