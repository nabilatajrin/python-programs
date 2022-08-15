class SelfParameter:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = SelfParameter("John", 36)
p1.myfunc()
