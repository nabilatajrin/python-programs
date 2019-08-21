fruits = ['aple', 'orange', 'banana', 'tango', 'jambura']

found = 'no'

for fruit in fruits:
    if fruit == 'jambura':
        found = 'yes'
        print('found it!')
        break

if found == 'yes':
    print('we have jambura!')
else:
    print('sorry')