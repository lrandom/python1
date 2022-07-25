print("Nhap vao mot so nguyen n")
n = int(input())
total = 0
count = 0
while count < n:
    if count % 2 == 0:
        total += count
    count += 1

print("Tổng là:", total)
