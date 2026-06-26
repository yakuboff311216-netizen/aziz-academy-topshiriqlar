n = int(input())
sonlar = list(map(int, input().split()))
k = int(input())

eng_yaqin = sonlar[0]
min_masofa = abs(sonlar[0] - k)

for i in range(1, n):
    masofa = abs(sonlar[i] - k)
    if masofa < min_masofa or (masofa == min_masofa and sonlar[i] < eng_yaqin):
        min_masofa = masofa
        eng_yaqin = sonlar[i]
        
print(eng_yaqin)  