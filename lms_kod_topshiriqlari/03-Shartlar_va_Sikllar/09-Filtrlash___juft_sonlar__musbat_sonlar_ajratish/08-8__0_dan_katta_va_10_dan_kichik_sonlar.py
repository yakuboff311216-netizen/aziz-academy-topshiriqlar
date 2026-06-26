n = int(input())
sonlar = list(map(int, input().split()))
for son in sonlar:
    if 0 < son < 10:
        print(son)