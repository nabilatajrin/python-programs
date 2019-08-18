from polymorphism.Polymorphism_1 import Cat


class Calculator:

    def set(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


#inheritted class Calculator here
class NewCalculator(Calculator):

    def multiply(self):
        return self.a * self.b

c = NewCalculator()
c.set(2, 3)
print (c.add())
print (c.multiply())