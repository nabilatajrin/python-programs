fruits = ["apple", "orange", "jambura", "banana", "mango", "cherry"]

#print(fruits[0+1])

found = "no"

for fruits in fruits:
    if fruits == "jambura":
        found = "yes"
        print("found it!")
        break

if found == "yes":
    print("we have jambura")
else:
    print("sorry")

