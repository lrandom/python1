def a(func):
    func()


def myFunc():
    print("Hello")


a(myFunc)

a(lambda: print("Hello"))
