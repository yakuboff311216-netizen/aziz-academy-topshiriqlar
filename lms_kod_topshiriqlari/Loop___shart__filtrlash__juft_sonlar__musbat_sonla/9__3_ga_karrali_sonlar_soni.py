n = int(input())
input_data = []

while len(input_data) < n:
    input_data.extend(map(int, input().split()))
    
count = 0
for son in input_data[:n]:
    if son % 3 == 0:
        count += 1
        
print(count)