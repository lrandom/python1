# function scope
# def hello():
#     name = "Thảo"
#     print("Hello")
#     print(name)
#
# hello()
# print(name)

# globl scope
name = "Thảo"


def hello():
    print("Hello", name)


hello()
print(name)
