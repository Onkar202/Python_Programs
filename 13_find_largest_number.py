n1=int(input("Enter a first number: "))
n2=int(input("Enter a second number: "))
n3=int(input("Enter a third number: "))


if n1>n2 and n1>n3:
    print(f"{n1} is a largest number")
elif n2>n3:
    print(f"{n2} is a largest number")
else:
    print(f"{n3} is a largest number")
