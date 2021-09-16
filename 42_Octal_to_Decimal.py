n = int(input("Enter a octal number: "))
dec,i=0,0
while n!=0:
    rem = n % 10
    dec = dec + rem * (8**i)
    n//=10
    i+=1
print(dec)