f = 0
print(f)

#re-declaring the variable works
f = 'abc'
print(f)
del f

#ERROR: variables of different types cannot be combined
#err:print("This is a string" + 123)
#correction:
print("This is a string " + str(123))

#Global vs local variables in functions
def someFunction():
    f = 'def'
    print(f)

someFunction()
print(f) #outside of the function

del f
print(f)