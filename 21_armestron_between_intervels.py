n = int(input("Enter a first three digit intervel: "))
n1 = int(input("Enter second three digit intervel: "))

for i in range(n,n1) :
         
        # number of digits calculation
        
             
        # compute sum of nth power of
        pow_sum = 0
        x = i
        while (x != 0) :
            digit = x % 10
            pow_sum = pow_sum + (digit ** 3)
            x = x // 10
             
        # checks if number i is equal to
        # the sum of nth power of its digits
        if (pow_sum == i) :
            print(str(i) + " "),