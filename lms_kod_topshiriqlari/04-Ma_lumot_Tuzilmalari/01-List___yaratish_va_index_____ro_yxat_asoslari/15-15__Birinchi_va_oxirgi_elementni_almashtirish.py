n = int(input())
lst = list(map(int, input().split()))
if len(lst) > 1:
    lst[0], lst[-1] = lst[-1], lst[0]
print(lst)