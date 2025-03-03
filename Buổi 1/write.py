import turtle

# Tạo màn hình
screen = turtle.Screen()

# Tạo một con rùa
turtle_pen = turtle.Turtle()

# Đặt tốc độ vẽ của rùa là 1 (tốc độ chậm nhất)
turtle_pen.speed(1)

# Hàm vẽ chữ X
def draw_X():
    turtle_pen.penup()
    turtle_pen.goto(-200, 0)
    turtle_pen.pendown()
    turtle_pen.setheading(60)
    turtle_pen.forward(50)
    turtle_pen.penup()
    turtle_pen.goto(-200, 0)
    turtle_pen.pendown()
    turtle_pen.setheading(-60)
    turtle_pen.forward(50)

# Hàm vẽ chữ i
def draw_i():
    turtle_pen.penup()
    turtle_pen.goto(-140, 0)
    turtle_pen.pendown()
    turtle_pen.setheading(90)
    turtle_pen.forward(50)
    turtle_pen.penup()
    turtle_pen.goto(-140, 60)
    turtle_pen.pendown()
    turtle_pen.dot(5)

# Hàm vẽ chữ n
def draw_n():
    turtle_pen.penup()
    turtle_pen.goto(-100, 0)
    turtle_pen.pendown()
    turtle_pen.setheading(90)
    turtle_pen.forward(50)
    turtle_pen.right(135)
    turtle_pen.forward(70)
    turtle_pen.left(135)
    turtle_pen.forward(50)

# Hàm vẽ chữ h
def draw_h():
    turtle_pen.penup()
    turtle_pen.goto(-40, 0)
    turtle_pen.pendown()
    turtle_pen.setheading(90)
    turtle_pen.forward(50)
    turtle_pen.penup()
    turtle_pen.goto(-40, 25)
    turtle_pen.pendown()
    turtle_pen.setheading(0)
    turtle_pen.forward(30)
    turtle_pen.setheading(90)
    turtle_pen.forward(25)

# Hàm vẽ chữ a
def draw_a():
    turtle_pen.penup()
    turtle_pen.goto(20, 0)
    turtle_pen.pendown()
    turtle_pen.setheading(60)
    turtle_pen.forward(50)
    turtle_pen.right(120)
    turtle_pen.forward(50)
    turtle_pen.backward(25)
    turtle_pen.right(120)
    turtle_pen.forward(25)

# Hàm vẽ chữ o
def draw_o():
    turtle_pen.penup()
    turtle_pen.goto(80, 0)
    turtle_pen.pendown()
    turtle_pen.circle(25)

# Vẽ từng chữ cái
draw_X()
draw_i()
draw_n()
draw_h()
draw_a()
draw_o()

# Giữ cửa sổ mở
turtle.done()