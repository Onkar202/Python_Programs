# n = int(input("Enter a number: "))
# n1 = 1
# n2 = 0
# result = 0
# for i in range(n+1):
#     print(result)
#     result = n1 + n2
#     n1 = n2
#     n2 = result

def fibona(n):
    n1 = 1
    n2 = 0
    fibo = 0
    for i in range(n+1):
        print(fibo)
        fibo = n1 + n2
        n1 = n2
        n2 = fibo
    
print(fibona(10))
