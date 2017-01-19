class A1:
    def __init__(self):
        self.a = 3
        self.__b = 1

class A2:
    def __init__(self):
        self.a = 2
        self.__b = 2

class B(A1, A2):
    def __init__(self):
        A1.__init__(self)
        A2.__init__(self)

o = B()
print o.__dict__

