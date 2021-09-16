n = int(input("Enter a Three digit numbers: "))
n1 = n
arm = 0
while(n1!=0):
    rem = n1%10
    arm += rem ** 3
    n1 //= 10
if(arm == n):
        print("Armstrong")
    