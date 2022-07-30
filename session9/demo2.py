def total(a, b):
    print("Tổng hai số là", a + b)


# first citizen function
myTotal = total  # phép gán

myTotal(10, 20)


# first citizen function
# sub gọi là higher order function
# func gọi là callback function
def sub(a, b, func):
    sub = a - b
    func(sub)


def myFunc(sub):
    print("Hiệu là", sub)


sub(10, 20, myFunc)


# first citizen function
def multiple(a, b):
    mul = a * b;

    def multipleTo2(mul):
        mul *= 2
        print(mul)

    multipleTo2(mul)


multiple(2, 10)
