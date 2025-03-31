class SinhVien:
    def __init__(self, ms, ten, diem):
        self.ms = ms
        self.ten = ten
        self.diem = diem
    def in_thong_tin(self):
        print(f"Ma so sinh vien: {self.ms}")
        print(f"Ho va ten sinh vien: {self.ten}")
        print(f"Diem trung binh: {self.diem}")


sv1 = SinhVien("SV01", "Nguyen Van A", 8.5)
sv1.in_thong_tin()
