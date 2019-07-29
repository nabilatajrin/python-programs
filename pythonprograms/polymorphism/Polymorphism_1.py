class Pet:

    def __init__(self, name):
        self.name = name

    def talk(self):
        pass


class Cat(Pet):

    def talk(self):
        print (self.name + ": meow!")


class Dog(Pet):

    def talk(self):
        print (self.name + ": hoof! hoof!")


class Tiger(Pet):

    def talk(self):
        print (self.name + ": halum!")


class Mouse(Pet):

    def talk(self):
        print (self.name + ": kich! kich!")


cat = Cat("bilai")
dog = Dog("kuttush")
tiger = Tiger("bug")
mouse = Mouse("idur")

cat.talk()
dog.talk()
tiger.talk()
mouse.talk()