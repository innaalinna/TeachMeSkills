print("Please enter how much numbers do you want:")
n = int(input())
i = 0
resPart1 = ''
resPart2=''

while i<n:
    print("Please enter number:")
    num = int(input())
    if num != 0:
        resPart1 += str(num)
    else:
        resPart2 +="0"

    i += 1

res = resPart2+resPart1
print("And result is: "+res)


