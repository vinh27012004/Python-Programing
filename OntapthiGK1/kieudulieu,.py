'''
Nhập một số nguyên n, kiểm tra n là số chẵn hay lẻ.

Viết chương trình nhập một số n, in ra bảng cửu chương của n.

Tính tổng các số chẵn từ 1 đến n (sử dụng vòng lặp for).

Kiểm tra một số n có phải số nguyên tố không.

Viết chương trình nhập một danh sách số nguyên, in ra số lớn nhất và nhỏ nhất.
'''
n = int(input("Nhập số nguyên n: "))
if n % 2 == 0:
    print(f"{n} là số chẵn")
else:
    print(f"{n} là số lẻ")

print(f"Bảng cửu chương của {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

tong = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        tong += i
print(f"{tong}")

for i in range(2 ,n):
    if n % i == 0:
        print(f"{n} không phải là số nguyên tố")
        break
else:
    print(f"{n} là số nguyên tố")

# Bước 1: Nhập chuỗi từ người dùng
input_string = input("Nhập danh sách số nguyên (cách nhau bởi dấu phẩy): ")

# Bước 2: Tách chuỗi thành danh sách các phần tử dựa trên dấu phẩy
string_list = input_string.split(',')

# Bước 3: Chuyển từng phần tử trong danh sách từ chuỗi sang số nguyên
numbers = list(map(int, string_list))

# In ra kết quả để kiểm tra
print("Danh sách số nguyên:", numbers)
max_number = max(numbers)
min_number = min(numbers)
print(f"Số lớn nhất: {max_number}")
print(f"Số nhỏ nhất: {min_number}")
