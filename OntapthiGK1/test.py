# Bước 1: Nhập chuỗi từ người dùng
input_string = input("Nhập danh sách số nguyên (cách nhau bởi dấu cáchh): ")

# Bước 2: Tách chuỗi thành danh sách các phần tử dựa trên dấu phẩy
string_list = input_string.split()

# Bước 3: Chuyển từng phần tử trong danh sách từ chuỗi sang số nguyên
numbers = list(map(int, string_list))

# In ra kết quả để kiểm tra
print("Danh sách số nguyên:", numbers)