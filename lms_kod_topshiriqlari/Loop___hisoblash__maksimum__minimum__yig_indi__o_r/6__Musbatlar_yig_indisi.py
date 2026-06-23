n = int(input())
sonlar = list(map(int, input().split()))

musbat_yigindi = 0

for son in sonlar:
    if son > 0:
        musbat_yigindi += son
        
print(musbat_yigindi)