n = int(input("Enter a number: "))
n1 = 0
while n!=0:
    rem = n%10
    n1 = n1 * 10 + rem
    
    n //=10
print(n1)