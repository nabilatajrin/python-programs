def is_prime(x):

    for x in range(2, 101):
        if is_prime(x):
            print (x)