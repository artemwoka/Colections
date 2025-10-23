input()
a = list(map(int,input().split()))

list_pst = [x + 1 for x in range(len(a)) if a[x] > 0]
list_ngt = [x + 1 for x in range(len(a)) if a[x] < 0]
list_ngt.reverse()

print(' '.join(list(map(str,list_pst))), '\n', ' '.join(list(map(str,list_ngt))))

