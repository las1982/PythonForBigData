class A:
    def __init__(self):
        self.__a = 1
    def __getattr__(self, name):
        if name in ('a', 'b'):
            return  self.__a

o = A()
print o.a
print o.b
print o.c
print getattr(o, 'a', 'b')
setattr(o, 'c', 3)
print o.c
# print o__hasattr__('d')

print o.__dict__

class A(object):
    __slots__ = ('a')
    def __init__(self):
        self.a = 1

obj = A()
obj.a = 1
print obj.a
obj.b = 1

class A(object):
    def __init__(self):
        self.__a = None
    def getx(self):
        return self.__a
    def setx(self, value):
        self.__a = value
    def delx(self):
        del self.__a
    x = property(getx, setx, delx, "'x' property")

o = A()
o.x = 1
print o.x
print A.__dict__

# linux: red heat, centras <!!!, debian - for university