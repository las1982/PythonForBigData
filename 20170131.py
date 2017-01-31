a = 1
print eval("1 + a")
print locals()
print globals()

s = '''
class A:
    def m(self, a):
        print self, a
'''

exec s
print locals()
# O = A()
O = eval("A()")
print O.m(2)


def f(a, b = 1):
    v = a + b
    print v

print f.__name__
print f.__defaults__