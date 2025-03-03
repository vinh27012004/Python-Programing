import turtle

# Tạo màn hình
screen = turtle.Screen()

# Tạo một con rùa
t = turtle.Turtle()

t.speed(1)

# Đặt màu cho rùa
t.fillcolor('red')
t.begin_fill()

# Vẽ nửa trái của trái tim
t.left(50)
t.forward(133)
t.circle(50, 200)

# Vẽ nửa phải của trái tim
t.right(140)
t.circle(50, 200)
t.forward(133)

t.end_fill()

# Giữ cửa sổ mở
turtle.done()
