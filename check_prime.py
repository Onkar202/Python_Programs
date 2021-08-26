n = int(input("Enter a number to check: "))
flag = True
for i in range(2,n-1):
    if(n % i == 0):
        print("Non-Prime")
        flag = False
        break
else:
    print("Prime")