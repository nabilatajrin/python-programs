from OOP.Person import Person

class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    super().__init__(fname, lname)
    self.graduationyear = 2019
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.printname()
