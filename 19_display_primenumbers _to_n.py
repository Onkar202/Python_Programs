def prime(n):
    fl = 1
    for i in range(2,n+1):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                print(i)
    return "These are the prime numbers"
a = prime(10)
print(a)

