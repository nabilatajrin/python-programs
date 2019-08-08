class Calculator:

    def set(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

c = Calculator()
c.set(2, 3)

print (c.add())