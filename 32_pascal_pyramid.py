n = int(input("Enter a number: "))
pas = 1
for i in range(1,n):
    for j in range(1,n-i+1):
        print(" ",end='')
    for j in range(0,i):
        if(j==0 or i==0):
            pas = 1
        else:
            pas = pas*(i-j)//j
        print(pas,end=' ')
    print()