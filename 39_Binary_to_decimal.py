n=int(input("Enter a binary number: "))
n1=n
i,dec=0,0
while n1!=0:
    rem = n1%10
    dec = dec + rem *(2**i)
    n1//=10
    i+=1
print(dec)

# '''  Using Function'''
# def bin_to_dec(n):
#     n1=n
#     dec,i=0,0
#     while(n!=0):
#         rem = n%10
#         dec = dec+rem * (2 ** i)
#         n=n//10
#         i+=1
#     print(dec)

# if __name__ == '__main__':
#     bin_to_dec(1111)
    