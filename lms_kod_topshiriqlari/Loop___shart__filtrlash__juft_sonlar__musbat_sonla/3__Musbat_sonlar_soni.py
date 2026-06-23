def musbat_sonlar_soni(sonlar):
    musbat_sonlar = [son for son in sonlar if son > 0]
    return len(musbat_sonlar)

n = input()
sonlar = list(map(int, input().split()))
print(musbat_sonlar_soni(sonlar))