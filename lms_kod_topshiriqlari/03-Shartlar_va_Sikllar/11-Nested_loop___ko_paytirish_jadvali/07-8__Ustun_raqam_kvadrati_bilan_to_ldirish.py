n, m = map(int, input().split())

print(" ".join(str(i*i) for i in range(2, m + 1)))