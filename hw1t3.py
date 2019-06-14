print("Please enter how much numbers do you want:")
n = int(input())
numList = []
i = 0
ord = []
resPart1 = ''
resPart2=''
cnt = 0

while i<n:
    print("Please enter number:")
    num = int(input())
    numList.append(num)
    if num != 0:
        resPart1 += str(num)
    else:
        resPart2 +="0"

    i += 1

res = resPart2+resPart1
print("And result is: "+res)


