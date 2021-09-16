'''Using recurssion'''
def dec_to_bin(n):
    if n>1:
        dec_to_bin(n//2)
    print(n%2,end=' ')

if __name__=='__main__':
    dec_to_bin(16)

# n = int(input("Enter a decimal number: "))
# n1 = []
# while n!=0:
#     rem = n % 2
#     n1.append(rem)
#     n//=2
# n2 = n1.reverse()
# for i in n1:
#     print(i,end=' ')

