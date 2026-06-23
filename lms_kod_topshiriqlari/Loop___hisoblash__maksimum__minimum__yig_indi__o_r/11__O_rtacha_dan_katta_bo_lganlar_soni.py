n = int(input())
sonlar = list(map(int, input().split()))

yigindi = sum(sonlar)
o_rtacha = yigindi / n

katta_sonlar_soni = sum(1 for son in sonlar if son > o_rtacha)

print(katta_sonlar_soni)