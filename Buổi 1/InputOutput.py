
n = 5
x , y = 20 , 30
x, y = y, x
height = 10.0
weight = 20
bmi = weight / (height ** 2)
print(bmi)
## CÂU LỆNH ĐIỀU KIỆN
#Dạng 1: Câu lệnh if đơn
n = 5
if (n > 0):
    print("Số dương")

#Dạng 2: Câu lệnh if else

n = 5
if n % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")

#Dạng 3: Câu lệnh if elif else

dtb = float(input("Nhập điểm trung bình: "))

if (dtb < 5):
    print("Học lực yếu")
elif (dtb < 7):
    print("Học lực trung bình") 
elif (dtb <= 8):
    print("Học lực khá")
else:
    print("Học lực giỏi")

## CÂU LỆNH LẶP

#Dạng 1: Vòng lặp for
#Cách 1: truy cập thông qua giá trị của phần tử
names = "Trần Đức Bo, Nguyễn Văn An, Phạm Thị Bình"
for n in names:
    print(n, end="")

#Cách 2: truy cập thông qua chỉ số của phần tử
for i in range(len(names)):
    print(names[i], end="")
can_full = "Canh, Tân, Nhâm, Quý, Giáp, Ất, Bính, Đinh, Mậu, Kỷ"
can = can_full.split(",")
print(can)

chi_full = "Thân, Dậu, Tuất, Hợi, Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi,"
chi = chi_full.split(",")
print(chi)

birth_year = int(input("Nhập năm sinh của bạn: "))
can_index = birth_year % 10
chi_index = birth_year % 12
print("Năm sinh của bạn là năm", can[can_index], chi[chi_index])

#Nhập 2 số nguyên dương m,n(m < n). In ra các số nguyên tố tỏng khoảng [m,n]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

m , n = 1, 50
for i in range(m, n + 1):
    if is_prime(i):
        print(i, end=" ")
