n = int(input("Enter a first number: "))
n1 = int(input("Enter a second number: "))
maximum = max(n,n1)
while(True):
    if(maximum%n==0 and maximum%n1==0):
        break
    maximum += 1
print(f"Lcm of {n} and {n1} is {maximum}")