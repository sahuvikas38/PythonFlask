n = int(input("enter the no more than 2:"))
a=0
b=1
if n<0:
    print("Incorrect value")
elif n==0:
    print(a)
elif n==1:
    print(b)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c=a+b
        a=b
        b=c
        print(c)
