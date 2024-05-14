# import turtle


# t = turtle.Turtle()

# turtle.bgcolor("lightblue")
# turtle.title("Simple House")

# # draw rectangle
# t.penup()
# t.goto(-100, -100)
# t.pendown()
# t.color("peru")
# t.begin_fill()
# for _ in range(2):
#     t.forward(200)
#     t.left(90)
#     t.forward(150)
#     t.left(90)
# t.end_fill()

# # draw roof
# t.penup()
# t.goto(-100, 50)
# t.pendown()
# t.color("brown")
# t.begin_fill()
# t.goto(0, 150)
# t.goto(100, 50)
# t.goto(-100, 50)
# t.end_fill()

# # draw door
# t.penup()
# t.goto(-30, -100)
# t.pendown()
# t.color("brown")
# t.begin_fill()
# for _ in range(2):
#     t.forward(60)
#     t.left(90)
#     t.forward(100)
#     t.left(90)
# t.end_fill()

# # draw windows
# def draw_window(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color("dark turquoise")
#     t.begin_fill()
#     for _ in range(4):
#         t.forward(40)
#         t.left(90)
#     t.end_fill()

# draw_window(-80, 0)
# draw_window(40, 0)


# t.hideturtle()

# turtle.done()
