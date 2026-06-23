n = int(input())
sonlar = list(map(int, input().split()))

min_qiymat = sonlar[0]
min_indeks = 0

for i in range(1, n):
    if sonlar[i] < min_qiymat:
        min_qiymat = sonlar[i]
        min_indeks = i
      
print(min_indeks)