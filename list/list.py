'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

mylist = ["apple", "banana", "cherry"]
#List
thislist = ["apple", "banana", "cherry"]
print(thislist)
#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]
#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
