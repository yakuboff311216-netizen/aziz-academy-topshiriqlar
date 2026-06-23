n, m = map(int, input().split())

s = m * (m + 1) // 2

for i in range(1, n + 1):
    print(i * s)