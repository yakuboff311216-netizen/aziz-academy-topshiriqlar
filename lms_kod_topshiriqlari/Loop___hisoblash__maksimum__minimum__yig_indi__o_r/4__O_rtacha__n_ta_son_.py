n = int(input())
sonlar = list(map(int, input().split()))

summa = 0

for son in sonlar:
    summa += son
    
    
if n > 0:
    ortacha = summa / n
    print(float(ortacha))
else:
    print("Sonlar miqdori 0 dan katta bo'lishi kerak.")