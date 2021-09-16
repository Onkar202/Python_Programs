n = int(input("Enter a number: "))
n1 = 1
for i in range(2,int(n/2)):
    if n%i == 0:
        n1 = 0
        print(f"{n} is a non prime number")
        break
else:
    print(f"{n} is a prime number")