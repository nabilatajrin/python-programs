#new line using back slash and n
x = 'hello \nworld'
print(x)

#print double quotes using escape character
y = 'hello \"world\"'
print(y)

#print double slash
a = 'hello \\ world'
print(a)
b = 'hello \\\ world'
print(b)

#print a tab's width
c = 'hello \t world'
print(c)

#remove white space, \b is the backspace
d = 'hello \bworld'
print(d)

#create a multi-line string
e = '''this
is
a
string'''
print(e)

#array of bytes
f = 'hello'
print(f[1])
#print multiple chars
print(f[0:1])
print(f[1:3])
print(f[1:])
print(f[2:])
print(f[-2:])

#length of the string
print(len(f))

text = 'hello, I am 10 years old today'
print('capitalize: ', text.capitalize())
print('upper: ', text.upper())
print('lower: ', text.lower())
print('title: ', text.title())

#find a word
y = text.find('hello')
z = text.find('years')
print(y) #will return positive any numbers when found
print(z)

if y>= 0:
    print('match')
else:
    print('not match')

#list/ array
z = ['apple','pear','banana']
#y = z.find('apple') /find doesn't work for list
y = z.index('apple')
print(y)
try:
    v = z.index('apples') #not found and gives error. so use try, catch
except ValueError:
    print('There is an error')

x = 'Hello, Brishty'
y = x.find('Bristy', 6, 12)
print(y)

#count words
x = 'How many apples are there in the apple cart?'
y = x.count('apple')
print(y)

#replace
z = x.replace('apple','pear')
print(z)

#variable
x = 'Zander'
y = '18'
print('Hello, my name is %s' % x) #for above py 3.5: print(f'Hello,...' % x)
print('Hello, my name is %s %s' % (x, y))
print('Hello, my name is {} {}'.format(x, y))
print('Hello, my name is {name} {age}'.format(name = x, age = y)) #or, print(f'Hello, my name is {x} {y}')








