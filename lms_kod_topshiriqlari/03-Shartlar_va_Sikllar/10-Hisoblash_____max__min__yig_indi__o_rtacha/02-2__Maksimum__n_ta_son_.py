n = int(input())
sonlar = list(map(int, input().split()))

max_son = sonlar[0]

for x in sonlar:
    if x > max_son:
        max_son = x
        
print(max_son)