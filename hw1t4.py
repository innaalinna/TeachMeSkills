print("Please enter how much numbers do you want:")
num = int(input())
#num = 3
print("Please enter X:")
x = float(input())
#x = 3.14
sign, i, n, nFact = -1.0, 0, 0, 1.0
res=0.0
while i<num:

    for i in range(1,n+1):
        nFact = nFact*i

    res += (sign**i)*(x**n)/nFact

    i+=1
    n+=2

print(res)