'''
Viết lớp SinhVien gồm các thuộc tính: MSSV, Tên, Điểm trung bình.

    Thêm phương thức hiển thị thông tin.

    Nhập danh sách sinh viên, tìm sinh viên có điểm cao nhất.

Viết lớp DongVat có phương thức keu(), lớp Cho và Meo kế thừa DongVat, ghi đè keu().

Viết chương trình quản lý danh sách nhân viên (MaNV, Tên, Lương), tính tổng lương nhân viên.

Viết lớp HinhHoc có phương thức dien_tich(), lớp HinhVuong, HinhTron kế thừa HinhHoc.

Xây dựng hệ thống quản lý sách: Lớp Sach (MaSach, TenSach, TacGia), danh sách sách, tìm kiếm sách theo tên.
'''

class SinhVien:
    def __init__(self , mssv, ten, diem_trung_binh):
        self.mssv = mssv
        self.ten = ten
        self.diem_trung_binh = diem_trung_binh
    def hien_thi_thong_tin(self):
        print(f"MSSV: {self.mssv}, Tên: {self.ten}, Điểm trung bình: {self.diem_trung_binh}")

n = int(input("Nhap so luong sinh vien: "))
danh_sach_sinh_vien = []
for i in range(n):
    mssv = input(f"Nhap MSSV sinh vien thu {i + 1}: ")
    ten = input(f"Nhap ten sinh vien thu {i + 1}: ")
    diem_trung_binh = float(input(f"Nhap diem trung binh sinh vien thu {i + 1}: "))
    sinh_vien = SinhVien(mssv, ten, diem_trung_binh)
    danh_sach_sinh_vien.append(sinh_vien)
    
print("Danh sach sinh vien:")
for sv in danh_sach_sinh_vien:
    sv.hien_thi_thong_tin()
# Tìm sinh viên có điểm cao nhất
diem_cao_nhat = max(danh_sach_sinh_vien, key=lambda sv: sv.diem_trung_binh)
print(f"Sinh vien co diem cao nhat: {diem_cao_nhat.hien_thi_thong_tin()}")

class DongVat:
    def keu(self):
        return "Keu"
class Cho (DongVat):
    def keu(self):
        return "Gau gau"
class Meo (DongVat):
    def keu(self):
        return "Meo meo"
print(Cho().keu())
print(Meo().keu())

class NhanVien:
    def __init__(self, ma_nv, ten, luong):
        self.ma_nv = ma_nv
        self.ten = ten
        self.luong = luong
    def hien_thi_thong_tin(self):
        print(f"Mã NV: {self.ma_nv}, Tên: {self.ten}, Lương: {self.luong}")
    @staticmethod
    def tinh_tong_luong(danh_sach_nv):
        return sum(nv.luong for nv in danh_sach_nv)

danh_sach_nhan_vien = []
n = int(input("Nhập số lượng nhân viên: "))
for i in range(n):
    ma_nv = input(f"Nhập mã nhân viên thứ {i + 1}: ")
    ten = input(f"Nhập tên nhân viên thứ {i + 1}: ")
    luong = float(input(f"Nhập lương nhân viên thứ {i + 1}: "))
    nhan_vien = NhanVien(ma_nv, ten, luong)
    danh_sach_nhan_vien.append(nhan_vien)

tong_luong = NhanVien.tinh_tong_luong(danh_sach_nhan_vien)
print(f"Tổng lương nhân viên: {tong_luong}")

class HinhHoc:
    def dien_tich(self):
        pass
class HinhVuong(HinhHoc):
    def __init__(self, canh):
        self.canh = canh
    def dien_tich(self):
        return self.canh ** 2
class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh
    def dien_tich(self):
        return 3.14 * self.ban_kinh ** 2
class HinhChuNhat(HinhHoc):
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong
class HinhTamGiac(HinhHoc):
    def __init__(self, day, chieu_cao):
        self.day = day
        self.chieu_cao = chieu_cao
    def dien_tich(self):
        return 0.5 * self.day * self.chieu_cao

tinh_vuong = HinhVuong(5)
tinh_tron = HinhTron(3)
tinh_hcn = HinhChuNhat(4, 6)
tinh_tg = HinhTamGiac(4, 5)
print("Diện tích hình vuông:", tinh_vuong.dien_tich())
print("Diện tích hình tròn:", tinh_tron.dien_tich())
print("Diện tích hình chữ nhật:", tinh_hcn.dien_tich())
print("Diện tích hình tam giác:", tinh_tg.dien_tich())

class Sach:
    def __init__(self, ma_sach, ten_sach, tac_gia):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
    def hien_thi_thong_tin(self):
        print(f"Mã sách: {self.ma_sach}, Tên sách: {self.ten_sach}, Tác giả: {self.tac_gia}")
    @staticmethod
    def tim_kiem_sach(danh_sach_sach, ten_sach):
        return [sach for sach in danh_sach_sach if ten_sach.lower() in sach.ten_sach.lower()]
n = int(input("Nhập số lượng sách: "))
danh_sach_sach = []
for i in range(n):
    ma_sach = input(f"Nhập mã sách thứ {i + 1}: ")
    ten_sach = input(f"Nhập tên sách thứ {i + 1}: ")
    tac_gia = input(f"Nhập tác giả sách thứ {i + 1}: ")
    sach = Sach(ma_sach, ten_sach, tac_gia)
    danh_sach_sach.append(sach)

ten_sach_tim_kiem = input("Nhập tên sách cần tìm: ")
sach_tim_thay = Sach.tim_kiem_sach(danh_sach_sach, ten_sach_tim_kiem)
if sach_tim_thay:
    print("Sách tìm thấy:")
    for sach in sach_tim_thay:
        sach.hien_thi_thong_tin()
else:
    print("Không tìm thấy sách với tên này.")   






