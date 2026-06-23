from collections import Counter

n= int(input())
sonlar = list(map(int, input().split()))

sonlar_soni = Counter(sonlar)

eng_ko_p_uchragan = min(son for son, count in sonlar_soni.items() if count == max(sonlar_soni.values()))

print(eng_ko_p_uchragan)