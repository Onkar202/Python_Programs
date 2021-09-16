# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n-1)
# n = int(input("Enter a number: "))
# print(sum(n))
n = int(input("Enter a number: "))
n1 = 0
for i in range (n+1):
    n1 += i
print(n1)