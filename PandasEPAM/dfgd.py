def aa(a):
    for i in range(a, 4):
        try:
            print 1.0 / i, i
        except:
            print 'exception'
            aa(1)
            continue

aa(0)