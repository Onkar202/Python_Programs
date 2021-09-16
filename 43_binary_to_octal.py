n = int(input("Enter a binary number: "))
i,dec=0,0
while n!=0:
    rem = n%10
    dec= dec + rem * (2**i)
    n//=10
    i+=1
print(dec)
oct=[]
while dec!=0:
    rem1 = dec%8
    oct.append(rem1)
    dec//=8
oct.reverse()
for i in oct:
    print(i,end=' ')