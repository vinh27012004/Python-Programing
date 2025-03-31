def xep_loai(diem_tb):
    ## Ràng buộc giá trị của điểm trung bìnhbình
    assert isinstance(diem_tb, (int, float)) and 0 <= diem_tb <= 10, "Diem trung binh phai nam trong khoang tu 0 den 10"
    return "Dat" if diem_tb >= 5 else "Khong dat"

x1 = xep_loai(7)
print(x1)



def swap(a, b):
    return b, a

x, y =5, 10
x, y = swap(x, y)
print(x, y)



