number1 = 0
number2 = 0
choice = None
while choice != 6:
    print("\033[H\033[xJ", end="") #xoá màn hình trước
    # Xoá màn hình
    print("1.Nhập vào hai số")
    print("2.Tính tổng hai số")
    print("3.Tính hiệu hai số")
    print("4.Tính tích hai số")
    print("5.Tính thương hai số")
    print("6.Thoát chương trình")

    choice = int(input("Nhập lựa chọn của bạn: "))
    if choice == 1:
        print("Vui lòng nhập vào hai số")
        number1 = int(input())
        number2 = int(input())
    elif choice == 2:
        print("Tổng hai số là: ", number1 + number2)
    elif choice == 3:
        print("Hiệu hai số là: ", number1 - number2)
    elif choice == 4:
        print("Tích hai số là: ", number1 * number2)
    elif choice == 5:
        print("Thương hai số là: ", number1 / number2)
