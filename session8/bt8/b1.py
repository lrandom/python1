print("Vui lòng nhập vào một số")
number = int(input())
total = 1
for i in range(2, number):
    if number % i == 0:
        total += i
if total == number:
    print("Số này là số hoàn hảo")
else:
    print("Số này không phải số hoàn hảo")
