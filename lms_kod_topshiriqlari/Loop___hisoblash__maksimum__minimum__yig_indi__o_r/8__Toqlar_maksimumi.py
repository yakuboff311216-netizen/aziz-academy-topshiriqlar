n = int(input())
s = input()
sonlar = [int(i) for i in s.split()]
toq_sonlar = [son for son in sonlar if son % 2 != 0]
if toq_sonlar:
    mx = max(toq_sonlar)
    print(mx)
else:
    print("No")