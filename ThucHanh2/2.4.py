list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Sử dụng list comprehension để tạo danh sách một chiều chứa các số chẵn
even_nums = [num for sublist in list_of_lists for num in sublist if num % 2 == 0]

print(even_nums)