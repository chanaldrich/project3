# 【ACHV】: multiplication table

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j:2}", end="    ")
#     print()
# -----------------------------------------------------------------
# 【ACHV】: car 
# import turtle

# def draw_rectangle(color, x, y, width, height):
#     turtle.penup()
#     turtle.goto(x,y)
#     turtle.pendown()
#     turtle.color(color)
#     turtle.begin_fill()
#     for _ in range(2):
#         turtle.forward(width)
#         turtle.right(90)
#         turtle.forward(height)
#         turtle.right(90)
#     turtle.end_fill()

# def draw_circle(color, x, y, radius):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.color(color)
#     turtle.begin_fill()
#     turtle.circle(radius)
#     turtle.end_fill()

# def draw_car():
#     draw_rectangle("blue", -70, 0, 140, 50)
#     draw_rectangle("lightblue", -50, 25, 100, 30)
#     draw_circle("black", -35, -70, 15)
#     draw_circle("black", 35, -70 ,15)

# turtle.speed(1)
# turtle.bgcolor("white")

# draw_car()
# turtle.hideturtle()
# turtle.done()
# -----------------------------------------------------------------
# 【ACHV】: Simultaneous equations 

def solve_linear_system(a, b, c, d, e, f):

    denominator = a * e - b * d

    if denominator == 0:
        return None

    X = (c * e - b * f) / denominator
    Y = (a * f - c * d) / denominator

    return X, Y

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))
e = float(input("Enter the value of e: "))
f = float(input("Enter the value of f: "))

solution = solve_linear_system(a, b, c, d, e, f)

if solution:
    X, Y = solution
    print(f"X = {X}, Y = {Y}")
else:
    print("No unique solution")

# # # a b  c
# # # X+3Y=5
# # # 2X-Y=3
# # # d  e f

# # # 7X+8Y=-9
# # # 9X-4Y=17
# -----------------------------------------------------------------
# 【ACHV】: 


























































































































































































































































