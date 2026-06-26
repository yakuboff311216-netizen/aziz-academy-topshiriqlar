n = int(input())
sonlar = list(map(int, input().split()))
juft_yigindi = 0

for son in sonlar:
    if son % 2 == 0:
        juft_yigindi += son
        
print(juft_yigindi)