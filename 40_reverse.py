# Python program to reverse a number

n = int(input("Enter a number: "))
rev = 0

while(n > 0):
	a = n % 10
	rev = rev * 10 + a
	n = n // 10

print(rev)

# This code is contributed by Shariq Raza
