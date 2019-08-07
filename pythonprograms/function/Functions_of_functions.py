def is_prime(x):
    isprime = "yes"

    for i in range(2, x):
        if x % i == 0:
            isprime = "no"

    if isprime == "yes":
        print (x)


for x in range(1, 10):
    if is_prime(x):
        print(x)
