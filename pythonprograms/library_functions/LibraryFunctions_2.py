from pip._vendor.distlib.compat import raw_input

#string
print('please enter two numbers below:')
a = raw_input()
b = raw_input()

c = a + b
print('total', c)

#int
print('\nplease enter two numbers below:')
a = int(raw_input())
b = int(raw_input())

c = (a + b)
print (c)