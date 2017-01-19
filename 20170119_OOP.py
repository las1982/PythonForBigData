class ClassName:
    """"a simple class example"""
    i = 12345

    def f(self):
        return 'hello world'

a = ClassName()

print a.f()


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print (x.r, x.i)
