print("Nhập vào số nguyên dương n: ")
n = int(input())
if n < 20:
    for i in range(0, n + 1):
        if (i % 5 == 0 and i % 7 == 0):
            print(i)
