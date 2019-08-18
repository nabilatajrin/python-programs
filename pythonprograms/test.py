class Calculator:
    def set(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

#another class
class NewCalculator(Calculator):
    def multiply(self):
        return self.a * self.b

c = NewCalculator()
c.set(2, 3)

print(c.add())
print(c.multiply())
