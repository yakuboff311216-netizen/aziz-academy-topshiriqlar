n = int(input())
sonlar = list(map(int, input().split()))
juftlar = []
for son in sonlar:
    if son % 2 == 0:
        juftlar.append(son)
        
if len(juftlar) > 0:
    mn = juftlar[0]
    for j in juftlar:
        if j < mn:
            mn = j 
    print(mn)
else:
    print("No")