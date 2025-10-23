input()
a = list(map(int,input().split()))

list_aref = sum(a) / len(a)
list_sum = [x for x in a if x > list_aref]
print(sum(list_sum))

