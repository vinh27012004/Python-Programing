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