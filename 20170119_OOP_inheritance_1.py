class P:
    def __init__(self):
        self.__a = 1
    def f(self):
        print 'hello'

class A1(P):
    def __init__(self):
        super(P).__init__(self)
        self.__a1 = 2

class A2(P):
    def __init__(self):
        super(P).__init__(self)
        self.__a2 = 2

class B(A1, A2):
    def __init__(self):
        super(A1).__init__(self)
        super(A2).__init__(self)

o = B()
o.__dict__