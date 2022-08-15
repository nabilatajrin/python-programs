#list/ array
z = ['apple','pear','banana']
#y = z.find('apple') /find doesn't work for list
y = z.index('apple')
print(y)
try:
    v = z.index('apples') #not found and gives error. so use try, catch
except ValueError:
    print('There is an error')


x = ['Nabila', 'Tajrin', 'Brishty']
y = input('Please enter your name: ')

try:
    print(x.index(y)) #search in the list
except ValueError:
    print('No match was found')
else:
    print('A match was found.')
