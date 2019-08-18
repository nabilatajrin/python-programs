class Pet:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

class Cat(Pet):
    def talk(self):
        print(self.name + ": meow")

class Dog(Pet):
    def talk(self):
        print(self.name + ": hoof hoof!")

class Elephant(Pet):
    def talk(self):
        print(self.name + ": eeeeeee eeee")

cat = Cat("bilai")
dog = Dog("kuttush")
elephant = Elephant("haati")

cat.talk()
dog.talk()
elephant.talk()