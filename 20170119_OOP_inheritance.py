class T:
    def __init__(self):
        self.a = 1

o = T()
print o.a

o1 = T()
o1.b = 3
print o1.b
# print o.b - exeption

def func(self):
    print self

func(o)
T.f = func
T.f(o)
o.f()

class TT:
    def __init__(self):
        self.__a = 1
o = TT()
#print o.__a
print o._TT__a