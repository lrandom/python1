# hello = lambda x, y: x if x > y else y
# print(hello(1, 2))

hello2 = lambda x, y: ('true' if x > 3 else 'False') if x > y else y


def hello3(x, y):
    tmp = None
    if x > 3:
        tmp = 'true'
    elif (x < 3 and x > y):
        tmp = 'False'

    if x > y:
        return tmp
    else:
        return y

print(hello2(1, 4)) #8
print(hello3(1,4))
