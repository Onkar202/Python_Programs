n = int(input("ENter a number: "))
reverse = 0
while(n > 0):
    rem = n%10
    reverse = (reverse * 10) + rem
    n //= 10
print(reverse)