# n = int(input("Enter a number: "))
# n1=0
# if n!=0:
#     for i in range(n+1):
#         n1 += i

# print(n1)

def sum1(n):
    if n==1:
     return 1
    else:
        return n + sum1(n-1)
print(sum1(10))
