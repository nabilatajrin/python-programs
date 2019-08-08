def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
        #return factorial(x), this doesn't work

print (factorial(5))
#print(5*4*3*2*1)