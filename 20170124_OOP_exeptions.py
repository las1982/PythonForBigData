while True:
    try:
        x = int(raw_input("gsdfsg: "))
        break
    except ValueError:
        print "!!!vvv"
    except (RuntimeError, TypeError, NameError):
        pass

