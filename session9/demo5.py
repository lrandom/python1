def total(*nums):
    for num in nums:
        print(num)


total(1, 2, 3, 4, 5)
total(1, 2, 3, 4, 5, 6, 7, 8)


def total2(**nums):
    for key, value in nums.items():
        print(key, value)


total2(a=1, b=2, c=3)
total2(a=1, b=2, c=3, d=4, e=5)
