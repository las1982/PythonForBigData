items = [1, 2, 3, 4, 5]
squared = []
for x in items:
	squared.append(x ** 2)
print squared
#[1, 4, 9, 16, 25]


items = [1, 2, 3, 4, 5]
def sqr(x): return x ** 2
print map(sqr, items)
#[1, 4, 9, 16, 25]


print map((lambda x: x **2), items)
#[1, 4, 9, 16, 25]


def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print value


print filter(lambda x: x < 0, range(-5,5))

print reduce(lambda x, y: str(x) + '_*_' + str(y), [1, 2, 3, 4])