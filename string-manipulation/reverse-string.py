class ReverseString:
    #Solution 01: using for loop
    #Time Complexity: O(n)
    #Auxiliary Space: O(1)
    def reverse(s):
        str=""
        for i in s:
            str = i+str
        return str

    s = 'Geeks'
    print('output: ', reverse(s))

    # Solution 02: using for loop
    #Pseudocode:
    #run a loop from 'len(inputStr)-1' to 0
    #one by one append characters from end to start in result string

    #initialize an empty string:
    inputStr = 'Hello'
    result = ''
    for i in range(len(inputStr)-1, -1, -1):
        result = result + inputStr[i]
    #peint reserved string:
    print(result)

    # Solution 03: using inbuilt reversed funtion of python
    # Pseudocode:
    #use inbuilt function reversed(), it will return list of character of input string in reversed order
    inputStr = 'Geeks'
    reversedChars = reversed(inputStr)
    #now join list of chars without space
    print(''.join(reversedChars)) #this join() concatenate function to form a string


    # Solution 04: using extended slicing in python
    # Time Complexity: O(n)
    # Auxiliary Space: O(1)
    #syntax: inputStr[start:end:step]
    inputStr = 'Food'
    print(inputStr[-1::-1]) #:: is for traverse by default from the endpoint to start point
    #-1: is for starting backward from the end
    # :-1 is for end at first index 0

    #Or, in short:
    def reverse(str):
        str = str[::-1]
        return str
    s = 'Name'
    print('output: ', reverse(s))

    # Solution 05: using function call
    # Time Complexity: O(n)
    # Auxiliary Space: O(1)

    # Pseudocode:
    #function to reverse a string
    #by converting string to list
    #then reverse it and again convert it to string
    def reverse(str):
        str = list(str)
        str.reverse()
        return ''.join(str)

    s = 'Nature'
    print('output: ', reverse(s))

    # Solution 06: using list comprehension()
    #list comprehension creates the list of elements of a string in reverse
    #order and then it's elements and joined using join().
    #And then reversed order string is formed.
    # Time Complexity: O(n)
    # Auxiliary Space: O(1)

    #function to reverse a string:
    def reverse(string):
        string = [string[i] for i in range(len(string)-1, -1, -1)]
        return ''.join(string)
    s = 'List'
    print('output: ', reverse(s))

    # Solution 07: using reverse method:
    # Time Complexity: O(n)
    # Auxiliary Space: O(1)
    def reverse(str):
        str = ''.join(reversed(str))
        return str
    s = 'ReversedMethod'
    print('output: ', reverse(s))

    # Solution 08: using recursion:
    # Time Complexity: O(n)
    # Auxiliary Space: O(n)
    def reverse(s):
        if len(s) == 0:
            return s
        else:
            res = (s[1:])+s[0]
            return res
    str = 'recursion'
    print('output: ', reverse(str))


