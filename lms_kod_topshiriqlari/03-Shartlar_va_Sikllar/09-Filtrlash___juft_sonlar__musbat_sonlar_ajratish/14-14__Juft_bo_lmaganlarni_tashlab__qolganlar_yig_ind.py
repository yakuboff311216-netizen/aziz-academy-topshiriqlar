n = int(input())
sonlar = list(map(int, input().split()))

juft_yigindi = sum(x for x in sonlar if x % 2 == 0)
print(juft_yigindi)