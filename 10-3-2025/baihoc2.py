def generat_value():
    yield "Hello"
    yield "NhaTrang"
    yield 79

result = generat_value()
for res in result:
    print(res)


#hàm chuyển số sang từ khóa
def tong(*value):
    return sum([i for i in value if isinstance(i, int)])

results = tong(1, 2, 3, 4, 5, 'A')
print(results)


#Truyen doi so theo tu khoa
def print_student_info(**sv):
    print(f"Ma so sinh vien: {sv.get('mssv')}")
    print(f"Ho va ten sinh vien: {sv.get('name')}") 
    print(f"Tuoi sinh vien: {sv.get('age')}")
    print(f"Diem trung binh: {sv.get('dtb')}")
print_student_info(mssv='SV01', name='Nguyen Van A', age=20, dtb=8.5)

    
