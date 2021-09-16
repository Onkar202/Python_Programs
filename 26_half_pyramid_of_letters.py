n = int(input("Enter size of pyramid: "))
asc = 65

for i in range(n+1):
    for j in range(i+1):
        alpha = chr(asc)
        print(alpha,end=' ')
    asc = asc + 1
    print('\r')