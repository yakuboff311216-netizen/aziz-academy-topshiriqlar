data = list(map(int, input().split()))
if data == [0]:
    print(0)
else:
    n = data[0]
    m = data[1] if len(data) > 1 else n

    for _ in range(n):
        print(" ".join(str(i) for i in range(1, m + 1)))