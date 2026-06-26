n = int(input())
lst = list(map(int, input().split()))
k = int(input())
if 0 <= k < len(lst):
    print(lst[k])
else:
    print('Error')