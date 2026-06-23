n = int(input())
sonlar = list(map(int, input().split()))
toq_yigindi = 0

for son in sonlar:
    if son % 2 != 0:
        toq_yigindi += son
        
print(toq_yigindi)