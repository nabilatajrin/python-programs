#find out greatest common divisor
a = 33
b = 12

while b != 0:
    remainder = a % b
    a = b           # choto ta boro hobe
    b = remainder   # bakita hobe choto

print (a)   # gcd