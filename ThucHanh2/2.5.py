complex_list = [3, {'64131233': {'name': 'Võ Văn Tòng', 'age': 19}}, 5, (1, 3, 5, 4), ['bưởi', 'táo', 'cam', 'chanh'], 21, 'Khánh Hòa']

sum_of_integers = sum(item for item in complex_list if isinstance(item, int))

filtered_list = [item for item in complex_list if isinstance(item, int)]

print(f"Tổng các số nguyên = {sum_of_integers}")
print(f"Danh sách sau xử lý: {filtered_list}")