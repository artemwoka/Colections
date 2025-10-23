n = int(input())
list_1 = [int(x) for x in input().split()]

for i in range(0, n):
    if list_1[i] % 2 == 0:
        print(list_1[i], end=' ')

print()
for i in range(-1, -(n+1), -1):
       if list_1[i] % 2 == 1:
            print(list_1[i], end=' ')    

