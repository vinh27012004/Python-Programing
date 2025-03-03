## Viết CT Python cho phép lặp lại các thao tác nhập 1 số nguyên từ bàn phím, cho đến khi nhập 0 thì dừng lại 
## a) Tính tổng các số đã nhập
## b) Tính trung bình cộng của các số đã nhập

tong = 0

while True:
    try: # để khối lệnh có khả năng xảy ra lỗilỗi
        n = int(input("Nhập số nguyên: "))
        if n == 0:
            break
    except: 
        pass

    tong += n
    print("Tổng các số đã nhập: ", tong)
    print("Trung bình cộng của các số đã nhập: ", tong/n)