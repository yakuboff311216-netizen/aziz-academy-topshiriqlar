n = int(input())
sonlar = list(map(int, input().split()))

min_son = sonlar[0]
for x in sonlar:
    if x < min_son:
        min_son = x
        
print(min_son)