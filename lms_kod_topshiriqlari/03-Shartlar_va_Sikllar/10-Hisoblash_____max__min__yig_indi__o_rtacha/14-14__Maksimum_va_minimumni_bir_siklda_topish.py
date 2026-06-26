n = int(input())
sonlar = list(map(int,input().split()))

max_qiymat = sonlar[0]
min_qiymat = sonlar[0]

for i in range(1, n):
    if sonlar[i] > max_qiymat:
        max_qiymat = sonlar[i]
    if sonlar[i] < min_qiymat:
        min_qiymat = sonlar[i]
        
print(max_qiymat, min_qiymat)