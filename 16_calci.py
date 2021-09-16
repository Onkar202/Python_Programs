n1 = float(input("Enter First number here: "))
op = input("Enter operation: ")
n2 = float(input("Enter second number here: "))
if(op=='+'):
    ans = n1 + n2
    print("Answer is ",ans)
elif(op=='-'):
    ans = n1 - n2
    print("Answer is ",ans)
elif(op=='*'):
    ans = n1 * n2
    print("Answer is ",ans)
elif(op=='/'):
    ans = n1 / n2
    print("Answer is ",ans)
else:
    print("Please enter valid operation")
