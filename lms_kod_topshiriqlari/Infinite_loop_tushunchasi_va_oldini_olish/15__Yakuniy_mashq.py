s = input()

if s.isdigit():
    a = list(map(int, input().split()))
    
    print(a[0])
    print(a[1:-1])
    print(a[-1])
else:
    while s != "stop":
        print("Working")
        s = input()