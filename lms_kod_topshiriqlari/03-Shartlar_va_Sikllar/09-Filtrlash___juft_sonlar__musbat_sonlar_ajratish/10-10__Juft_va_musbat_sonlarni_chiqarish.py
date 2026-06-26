n = int(input())

input_data = []
while len(input_data) < n:
    input_data.extend(map(int, input().split()))
    
sonlar = input_data[:n]

for son in sonlar:
    if son % 2 == 0 and son > 0:
        
        print(son)