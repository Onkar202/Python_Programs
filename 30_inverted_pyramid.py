n = int(input("Enter size of pyramid: "))

for i in range(n,1,-1):
    for j in range(n-i):
        print(end=' ')
    for j in range(i,2*i-1):
        print("*",end='')

    for j in range(1,i-1):
        print("*",end='')

    
    print('\r')