n = int(input())
sonlar = [int(i) for i in input().split()]

mx = sonlar[0]
mx_index = 0

for i in range(1, n):
    if sonlar[i] > mx:
        mx = sonlar[i]
        mx_index = i
        
print(mx_index)