n = int(input("Nhập số nguyên dương: "))
while n <= 0:
        print("Vui lòng nhập một số nguyên dương.")
        n = int(input("Nhập số nguyên dương: "))

while n > 0:
        print("Hình tam vuông")
        for i in range(1, n + 1):
                print('*' * i)
        print("Hình vuông")
        for i in range(n):
                print('*' * n)
        print("2 tam giác cụng đầu")
        for i in range(n):
                print(' ' * i + '*' * (2 * (n - i) - 1))
        for i in range(1, n):
                print(' ' * (n - i - 1) + '*' * (2 * i + 1))
        break