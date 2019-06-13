print("Please enter how much u wanna numbers:")
n = int(input())
nList = []
for i in range(1, n + 1):
    print("Please enter number:")
    l = int(input())
    nList.append(l)
nList.sort(reverse=True)
if n >= 2:
    print("two max are: " + str(nList[0]) + " and " + str(nList[1]))
elif n >= 0:
    print("max is: " + str(l))
else:
    print("idonno")
