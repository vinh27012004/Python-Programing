import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    

class Triangle(Shape):    
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

shapes = [
    Rectangle(3, 4),
    Circle(5),
    Triangle(5, 5),
    Rectangle(66, 7),
    Circle(2),
    Triangle(6, 8)
]
# In thông tin từng hình vẽ kèm theo: Loại, diện tích
for shape in shapes:
    print(f"Type: {type(shape).__name__}, Area: {shape.area()}")

# Đếm số lượng của mỗi loại hình vẽ
shape_counts = {"Rectangle": 0, "Circle": 0, "Triangle": 0}
for shape in shapes:
    shape_counts[type(shape).__name__] += 1
print("Shape counts:", shape_counts)
#Diện tích hình vẽ lớn nhât
max_shape = max(shapes, key=lambda shape: shape.area())
print(f"Shape with max area: {type(max_shape).__name__}, Area: {max_shape.area()}")

# Tìm hình vẽ có diện tích lớn nhất của mỗi loại
max_shapes = {"Rectangle": None, "Circle": None, "Triangle": None}
for shape in shapes:
    shape_type = type(shape).__name__
    if max_shapes[shape_type] is None or shape.area() > max_shapes[shape_type].area():
        max_shapes[shape_type] = shape

for shape_type, shape in max_shapes.items():
    print(f"Max area {shape_type}: {shape.area()}")

