n = int(input())
max_boluvchi = 0
for i in range(n - 1, 0, -1):
    if n % i == 0:
        max_boluvchi = i
        break
print(max_boluvchi)