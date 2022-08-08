x = input('Enter your name: ')
y = input('Enter your password: ')
z = input('Enter your password again: ')

if y == z:
    if len(y) < 8 or len(z) < 8:
        print('Password must be at least 8 characters long.')
    else:
        print('Thank you, an account has been created.')
    #pass
else:
    print('Passwords do not match - please try again.')
