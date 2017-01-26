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
print o__hasattr__('d')
