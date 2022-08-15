x = input('Enter your phone number: ')
y = len(x)
z = x[3:] #slicing
z2 = x[:3]
z3 = x[-3:]
z4 = len(x) - 3

print(z)
print(z2)
print(z3)
print(z4)
print(('*') * z4 + z3)

a = input('Enter your first name: ')
b = input('Enter your surname: ')

a = a[:1]
b = b[:1]
print((a + b).upper())
