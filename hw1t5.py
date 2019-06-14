import re

# exp = input()
exp = "1+4*4/2-15/5*2"
nmbrs = re.split(r'\+|\-|\*|\/', exp)
resNmbrs = nmbrs.copy()
oper = re.split(r'\d+', exp)
cntOper = oper.copy()
dictOper = list()
prt = 0

for i in enumerate(oper):
    if i[1] == "":
        oper.pop(int(i[0]))

for i in enumerate(oper):
    if i[1] == "/":
        prt = 1
    elif i[1] == "*":
        prt = 2
    elif i[1] == "+":
        prt = 3
    elif i[1] == "-":
        prt = 4
    else:
        continue
    dictOper.append((prt, i[0]))
dictOper.sort()
res = ''
m = 0
while dictOper.__len__()>0:
    i = dictOper[m]
    expOrd = i[1]
    num1 = int(resNmbrs[expOrd])
    num2 = int(resNmbrs[expOrd + 1])

    if i[0] == 1:
        res = num1 // num2
    elif i[0] == 2:
        res = num1 * num2
    elif i[0] == 3:
        res = num1 + num2
    elif i[0] == 4:
        res = num1 - num2

    resNmbrs[expOrd] = res
    resNmbrs.pop(expOrd + 1)

    for j in range(1, dictOper.__len__()):
        if dictOper[j][1] > i[1]:
            dictOper[j]=(dictOper[j][0],int(dictOper[j][1])-1)

    dictOper.pop(m)

print("And the result is: " + str(resNmbrs[0]))
