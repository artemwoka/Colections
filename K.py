input()
a = list(map(int,input().split()))

list_max = [x + 1 for x in range(len(a)) if a[x] == max(a)]
list_min = [x + 1 for x in range(len(a)) if a[x] == min(a)]

print(len(list_max),'\n',' '.join(list(map(str,list_max))), '\n',len(list_min),'\n' ,' '.join(list(map(str,list_min))))
