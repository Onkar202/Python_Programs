# n1 = int(input())
# n2 = int(input())
# n3=min(n1,n2)
# for i in range(1,n3+1):
#     if n1 % i ==0 and n2 % i ==0 :
#         hcf = i
# print(hcf)

def gcd(n1,n2):
    if (n2 != 0):
       return gcd(n2, n1 % n2)
    else:
       return n1
print(gcd(4,28))