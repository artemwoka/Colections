input()
a = list(map(int, input().split()))

sum_ = sum(a)
min_idx = a.index(min(a))
a.reverse()
max_idx = len(a) - a.index(max(a))
print(sum(a[min_idx:max_idx]))