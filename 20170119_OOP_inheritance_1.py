class P:
    def __init__(self):
        self.__a = 1
    def f(self):
        print 'hello'

class A1(P):
    def __init__(self):
        P.__init__(self)
        self.__a1 = 2

class A2(P):
    def __init__(self):
        P.__init__(self)
        self.__a2 = 2

class B(A1, A2):
    def __init__(self):
        A1.__init__(self)
        A2.__init__(self)

o = B()
print o.__dict__
