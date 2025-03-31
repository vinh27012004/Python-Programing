'''
Nhập một chuỗi, đếm số lần xuất hiện của từng ký tự.

Viết hàm kiểm tra một chuỗi có đối xứng (palindrome) không.

Viết chương trình nhập danh sách họ tên, sắp xếp danh sách theo tên (dùng split).

Nhập danh sách số nguyên, xóa các phần tử trùng lặp.

Nhập một từ điển lưu thông tin sinh viên {MSSV: Tên}, tìm sinh viên theo MSSV
'''

def dem_tu(string):
    dem_chuoi = {}
    for char in string:
        if char in dem_chuoi:
            dem_chuoi[char] += 1
        else:
            dem_chuoi[char] = 1
    return dem_chuoi

def kiem_tra_doi_xung(string):
    if string == string[::-1]:
        return True
    else:
        return False

string_input = input("Nhập một chuỗi: ")
dem = dem_tu(string_input)
print("Số lần xuất hiện của từng ký tự:" + str(dem))
kiem_tra = kiem_tra_doi_xung(string_input)
print(f"Chuỗi {string_input} có đối xứng không? {kiem_tra}")


def danh_sach_theo_ten(danhsach):
    return sorted(danhsach, key=lambda ho_ten: ho_ten.split()[-1])
danh_sach_ho_ten = []
n = int(input("Nhập số lượng họ tên: "))
for i in range(n):
    ho_ten = input(f"Nhập họ tên thứ {i + 1}: ")
    danh_sach_ho_ten.append(ho_ten)
danh_sach_sap_xep = danh_sach_theo_ten(danh_sach_ho_ten)
print("Danh sách họ tên đã sắp xếp theo tên:")
for ho_ten in danh_sach_sap_xep:
    print(ho_ten)

def xoa_trung_lap(danhsach):
    return list(set(danhsach))
danhsach_so_nguyen = []
n = int(input("Nhập số lượng số nguyên: "))
for i in range(n):
    so_nguyen = int(input(f"Nhập số nguyên thứ {i + 1}: "))
    danhsach_so_nguyen.append(so_nguyen)
danhsach_khong_trung_lap = xoa_trung_lap(danhsach_so_nguyen)
print("Danh sách số nguyên không trùng lặp:")
for so_nguyen in danhsach_khong_trung_lap:
    print(so_nguyen)


def tim_sinh_vien_theo_MSSV(danh_sach, MSSV):
    return danh_sach.get(MSSV, "Không tìm thấy sinh viên với MSSV này")

danh_sach_sinh_vien = {}
n = int(input("Nhập số lượng sinh viên: "))
for i in range(n):
    MSSV = input(f"Nhập MSSV thứ {i + 1}: ")
    ten = input(f"Nhập tên sinh viên thứ {i + 1}: ")
    danh_sach_sinh_vien[MSSV] = ten
MSSV_tim_kiem = input("Nhập MSSV cần tìm: ")
sinh_vien = tim_sinh_vien_theo_MSSV(danh_sach_sinh_vien, MSSV_tim_kiem)
print(sinh_vien)