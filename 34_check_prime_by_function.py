def check_prime(n):
    n1 = 1
    p = ''
    for i in range(2,int(n/2)):
        if(n%i==0):
            p=" Is Non - Prime"
            n1 = 0
    if(n1 == 1):
        p=" Is Prime"
    print(n,end='')
    return p

print(check_prime(5))