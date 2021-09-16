n = int(input("Enter size of pyramid: "))
k = 0
count=0
count1=0

for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(end=' ')
        count+=1

    for j in range(2*i-1):
        if count<=n-1:
            print(i+k, end="")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end="")
        k += 1
    count1 = count = k = 0
    print()
    
    print('\r')