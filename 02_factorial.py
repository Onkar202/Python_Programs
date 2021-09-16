def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n-1)

n1 = int(input("Enter a number: "))
print(fact(n1))
# n1 = 1
# for i in range(1,n+1):
#     n1 *= i
# print(n1)
    