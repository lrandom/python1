# count = 0;
# while count < 5:
#     print(count)
#     count += 1;
# else:
#     print("Kết thúc vòng lặp while")
#
# # Với một tham số trong range
# print("Với một tham số trong range")
# for i in range(5):
#     print(i)
#
# # Với hai tham số trong range
# print("Với hai tham số trong range")
# for k in range(1, 10):
#     print(k)
#
# # Với ba tham số trong range
# print("Với ba tham số trong range")
# for j in range(1, 10, 2):
#     print(j)
#
# # step lùi
# print("Step lùi")
# for k in range(10, 0, -1):
#     print(k)
#
# hoc_sinh = ["Luan", "Huy", "Hieu", "Hoa", "Hieu"]
# for vi_tri_mot_hoc_sinh, mot_hoc_sinh in enumerate(hoc_sinh):
#     print(vi_tri_mot_hoc_sinh, "=>", mot_hoc_sinh)
#
# for i in range(0, len(hoc_sinh)):
#     print(i, "=>", hoc_sinh[i])
#
# for i in range(6):
#     for j in range(6):
#         for k in range(6):
#             print("hello")

print("Demo break and continue")
for i in range(6):
    print(i)
    if (i == 3):
        continue
