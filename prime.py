def is_prime(num):
    #sqrt = x**(1/2.0)
    #To save time, test only up to sqrt(n), rounded up
    for i in range(2, int(num**(1/2.0))):
#   for i in range(2, num):
        if num%i==0:
            return 1

num = int(raw_input())
for i in range(2,num):
    if is_prime(i)==None:
        print i
