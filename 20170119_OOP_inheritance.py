class P:
    def __init__(self):
        self.__a = 1
    def f(self):
        print 'hello'

P.__dict__
o = P()
o.f()
o.__dict__

class C(P):
    def __init__(self):
        self.__b = 2
        P.__init__(self)
        super(P).__init__(self)

o = C()
o.f()
o.__dict__