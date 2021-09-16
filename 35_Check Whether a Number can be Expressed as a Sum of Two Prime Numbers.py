def Is_Prime(n):
    f1 = True
    f2 = 0
    for i in range(2,int(n)):
        if(n % i == 0):
            f1 = False
            f2 = 1
    if(f2==0):
        f1=True
    return f1

n = int(input("Enter a number: "))
f1 = False
for i in range(2,n):
    if(Is_Prime(i)):
        if(Is_Prime(n-i)):
            print(n," = ",i," + ",n-i)
            f1 = True