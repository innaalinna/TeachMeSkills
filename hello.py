print("hello world!")

m=1
print("Please enter X:")
x = float(input())

print("Please enter power m:")
m = int(input())
n = m
st = 1
fct = st
next_sign = 1
out = 0
while (n-2) >= 1:

    fct *= st*(st+2)
    print(st)
    print(fct)

    out_p = (x**st/fct)*next_sign

    out += out_p
    st += 2
    n -= 1
    next_sign = next_sign*(-1)
print("The result is: "+str(out))
