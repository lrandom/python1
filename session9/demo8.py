def total(a, b):
    return a + b


my_total = total(10, 20)
print(my_total)

my_total_2 = total(10, 20)
my_total_2 *= 2
print(my_total_2)


def calc(a, b, c):
    return a + b + c, a * b * c


total_1, multiple_1 = calc(10, 20, 30)
print(total_1, multiple_1)
