#Hàm lambda

sqr = lambda x: x**2

print(sqr(5))

#Hàm map
numbers = [1, 2, 3, 4, 5]

#Tạo danh sách chứa các giá trị bình phương

square_number = []
for i in numbers:
    square_number.append(i**2)
print(square_number)


#c2: list comprehension
square_number_2 = [i**2 for i in numbers]
print(square_number_2)

#C3: Hàm map
#tạo hàm trả về 
square_number_3 = list(map(lambda x: x**2, numbers))
print(square_number_3)

#Kết hợp hàm lambda
square_number_4 = list(map(lambda x: x**2, numbers))
print(square_number_4)

def  is_odd(n):
    return n % 2 != 0
odd_numbers = list(filter(is_odd, numbers)) 
print(odd_numbers)

odd_numbers_2 = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers_2)
