#Packing a tuple:
fruits = ("apple", "banana", "cherry")
#Unpacking a Tuple
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
