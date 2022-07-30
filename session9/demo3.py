def hello(sayHiText, name="World"):
    print(sayHiText + " " + name)


hello("Hi")  # Hi World
hello("Hi", "Python")  # Hi Python


#keyword agrument
def total(a, b=10, c=30):
    print("Tổng ba số là", a + b + c)


total(10, c=20)
