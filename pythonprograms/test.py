def is_prime(x):
    isprime = 'yes'

    #rang is 2 to target value-1, is x is divisible by any of these then it's not prime
    for i in range(2, x):
        if x % i == 0:
            isprime = 'no'

    if isprime == 'yes':
        print(x)

#range starts at 2
for x in range(1, 10):
    if is_prime(x):
        print(x)