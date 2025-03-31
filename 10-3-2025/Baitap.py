"""
Bài tập: Viết chương trình quản lý các danh sách các hình tròn trong mặt phẳng.
Mỗi hìh tròn có các dữ liệu sau:
- Tâm: là 1 điểm trong mặt phẳng (tạo lớp Point)
- Bán kính: là 1 số thực dương

Tạo danh sách n hình tròn:
-Tìm hình tròn có khoảng cách từ tâm đến góc tọa độ lớn nhất
-Liệt kê tất cả các cặp hình tròn giao nhaunhau
"""
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return np.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

p0 = Point(0, 0)
p1 = Point(3, 4)

print(p0.distance(p1))