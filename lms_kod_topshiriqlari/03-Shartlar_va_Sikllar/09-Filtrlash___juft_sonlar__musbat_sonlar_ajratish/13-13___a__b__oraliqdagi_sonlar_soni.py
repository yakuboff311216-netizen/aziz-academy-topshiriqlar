n = int(input())
sonlar = list(map(int, input().split()))
a, b = map(int, input().split())

counter = 0
for x in sonlar:
    if a <= x <= b:
        counter += 1
        
print(counter)