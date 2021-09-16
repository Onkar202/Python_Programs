n = int(input("Enter size of pyramid: "))
for i in range(n):
    for j in range(i+1):
        print("* ",end='')
    print('\r')