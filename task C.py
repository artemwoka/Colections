n = input("Enter numbers: ")
list_1 = [int(x) for x in n.split(" ")]

m = input("Enter numbers: ")
list_2 = [int(x) for x in m.split(" ")]

result = [list_1 , list_2]
result = sorted(result, key=len)
for i in result:
    print(", ".join(str(x) for x in i))