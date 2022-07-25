# Nhập vào số nguyên dương n từ bàn phím. Kiểm tra xem số n
# có phải là số nguyên tố hay không. Nếu là số nguyên tố thì in ra dòng text: Đây là số nguyên tố. Nếu không thì in ra: Không phải số nguyên tố.

print("Vui long nhap vao mot so nguyen duong")
n = int(input())
# số nguyên tố là số chia hết cho 1 và chính nó: 3,5,7
flag = True  # đặt biến flag là True = mặc định là số nguyên tố
count = 2  # đặt biến count là 2
while count < n:
    # nếu tìm được một cái ước
    if n % count == 0:
        flag = False  # đặt biến flag là False = không phải số nguyên tố
        break
    count += 1

if flag:
    print("Đây là số nguyên tố")
else:
    print("Đây không phải là số nguyên tố")
