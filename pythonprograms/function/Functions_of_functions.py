#prime numbers
def is_prime(x):
    isprime = "yes"

    for i in range(2, x): #should be divide by 1 since all digits/numbers are divisible by 1, should starts from 2
        if x % i == 0:
            isprime = "no"

    if isprime == "yes":
        print (x)

#starts at 1
for x in range(1, 10):
    if is_prime(x):
        print(x)
