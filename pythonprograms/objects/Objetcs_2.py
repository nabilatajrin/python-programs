class Calculator:

    def set(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

first = Calculator()
second = Calculator()

first.set(2, 2)
second.set(5, 12)

print (first.add())
print (second.add())