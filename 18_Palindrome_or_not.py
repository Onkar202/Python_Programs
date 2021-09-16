n = int(input("Enter a positive number: "))
rev = 0
n1 = n
while(n1!=0):
    rem = n%10
    rev = (rev * 10)+rem
    n1//=10

if(rev == n):
    print(n," is palindrome number")
else:
    print(n," Is not palindrome number")