# 【ACHV】: multiplication table

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j:2}", end="    ")
#     print()
# -----------------------------------------------------------------
# 【ACHV】: the turtle
# square

# import turtle
# window = turtle.Screen()
# john = turtle.Turtle()

# john.forward(100)
# john.right(90)
# john.forward(100)
# john.right(90)
# john.forward(100)
# john.right(90)
# john.forward(100)
# john.right(90)
# or (its the same)
# for i in [0,1,2,3]:
    # john.forward(100)
    # john.right(90)
# or (its the same)
# for i in range(4):
#     john.forward(100)
#     john.right(90)
# window.exitonclick()
# --------------------------------------
# diffuse square

# import turtle
# window = turtle.Screen()
# john= turtle.Turtle()

# for i in range(1,21):
#     john.forward(i*10)
#     john.right(90)

# window.exitonclick()
# --------------------------------------
# rotated squares

# import turtle
# window = turtle.Screen()
# john= turtle.Turtle()

# for i in range (12):
#     for j in range (4):
#         john.forward(100)
#         john.right(90)  
#     john.right(30)

# window.exitonclick()
# --------------------------------------
# parallel square(1)

# import turtle
# window = turtle.Screen()
# window.setup(480, 360)

# john= turtle.Turtle()
# john.penup()
# john.goto(-140, 20)

# for i in range(6):
#     john.pendown()
#     for j in range(4):
#         john.forward(30)
#         john.right(90)
#     john.penup()
#     john.forward(60)

# window.exitonclick()
# --------------------------------------
# 


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

# def solve_linear_system(a, b, c, d, e, f):

#     denominator = a * e - b * d

#     if denominator == 0:
#         return None

#     X = (c * e - b * f) / denominator
#     Y = (a * f - c * d) / denominator

#     return X, Y

# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# c = float(input("Enter the value of c: "))
# d = float(input("Enter the value of d: "))
# e = float(input("Enter the value of e: "))
# f = float(input("Enter the value of f: "))

# solution = solve_linear_system(a, b, c, d, e, f)

# if solution:
#     X, Y = solution
#     print(f"X = {X}, Y = {Y}")
# else:
#     print("No unique solution")

# # # a b  c
# # # X+3Y=5
# # # 2X-Y=3
# # # d  e f

# # # 7X+8Y=-9
# # # 9X-4Y=17
# -----------------------------------------------------------------
# 【ACHV】: Simultaneous Equations Three Variables

# def solve_three_variable_system(a, b, c, d, e, f, g, h, i, j, k, l):

#     D = a*(f*k - g*j) - b*(e*k - g*i) + c*(e*j - f*i)

#     if D == 0:
#         return "No unique solution"

#     D_X = d*(f*k - g*j) - b*(h*k - g*l) + c*(h*j - f*l)
#     D_Y = a*(h*k - g*l) - d*(e*k - g*i) + c*(e*l - h*i)
#     D_Z = a*(f*l - h*j) - b*(e*l - h*i) + d*(e*j - f*i)

#     X = D_X / D
#     Y = D_Y / D
#     Z = D_Z / D

#     return X, Y, Z

# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# c = float(input("Enter the value of c: "))
# d = float(input("Enter the value of d: "))
# e = float(input("Enter the value of e: "))
# f = float(input("Enter the value of f: "))
# g = float(input("Enter the value of g: "))
# h = float(input("Enter the value of h: "))
# i = float(input("Enter the value of i: "))
# j = float(input("Enter the value of j: "))
# k = float(input("Enter the value of k: "))
# l = float(input("Enter the value of l: "))

# solution = solve_three_variable_system(a, b, c, d, e, f, g, h, i, j, k, l)

# if isinstance(solution, str):
#     print(solution)
# else:
#     X, Y, Z = solution
#     print(f"X = {X}, Y = {Y}, Z = {Z}")

# a    b    c    d
# 1x + 6y - 6z = -11
# e    f    g    h
# 3x + 3y + 3z = 42
# i    j    k    l
# 4x + 6y + 5z = 65

# 6x + 1y + 4z = 38
# 1x + 2y - 1z = 11
# 4x + 5y + 6z = 80
# -----------------------------------------------------------------
# 【ACHV】: Law of Cosine

# import math

# def caoculate_third_side(a, b, d):
#     d_rad = math.radians(d)

#     c = math.sqrt(a**2 + b**2 - 2 * a * b *  math.cos(d_rad))

#     c = round(c, 2)

#     return c

# a = float(input("Enter the length of side of a: "))
# b = float(input("Enter the length of side of b: "))
# d = float(input("Enter the angle between side of a and b(in degrees): "))

# c = caoculate_third_side(a, b, d)

# print(f"The length of the third side c is: {c}")

# a=5  b=8 d=60

# a=5  b=7 d=21.8
# -----------------------------------------------------------------
# 【ACHV】: squared math

# def calculate_expression(a, b, c, d):
#     result = (a + b) * (c ** 2) +d
#     return round(result, 2)

# result = calculate_expression(1, 2, 3, 5)
# print(result)
# -----------------------------------------------------------------
# 【ACHV】: the data type of a + b

# result = 4 + 6.5
# print(type(result))
# -----------------------------------------------------------------
# 【ACHV】: Use input() to read a value and store it in variable a, and finally use the print command to print out ''My lucky number v is ▯''.

# a = input("please enter avalue:")
# print(f"my lucky number is {a}")

# -----------------------------------------------------------------
# 【ACHV】: Take out every character of ''Python''.

# string = "python"
# for char in string:
#     print(char)
# chars = [char for char in string]
# print(chars)

# -----------------------------------------------------------------
# 【ACHV】: Take out the three words from ''I love python''.

# sentence = "i love python"
# words = sentence.split()

# first_three_words = words[:3]
# print(first_three_words)

# -----------------------------------------------------------------
# 【ACHV】: Use loops to print l love you so so so…much. so to be repeated 100 times!

# repeat_so = 'so ' * 100

# print(f"i love you {repeat_so}much.")
# -----------------------------------------------------------------
# 【ACHV】: Use f_string to output 123.456789 to 3 decimal places.

# number = 123.456789
# formatted_number = f"{number:.3f}"
# print(formatted_number)
# -----------------------------------------------------------------
# 【ACHV】: Represent 0.25 as 25% using f_string.

# number = 0.25
# formatted_percentage = f"{number:.0%}"
# print(formatted_percentage)
# -----------------------------------------------------------------
# 【ACHV】: Calculate the maximum, minimum and average scores, and sort the scores from small to large.

# scores = [68, 72, 84, 96, 88]

# max_score = max(scores)
# min_score = min(scores)
# average_score = sum (scores) / len(scores)

# sorted_score = sorted(scores)

# print(f"highest score:{max_score}")
# print(f"lowest score:{min_score}")
# print(f"average score:{average_score}")
# print(f"sorted score:{sorted_score}")
# -----------------------------------------------------------------
# 【ACHV】: Change the separator symbol into a semicolon

# subjects = 'Chinese, English, Math, Social studies, Nature and technology'

# formatted_subjects =subjects.replace(',', '、')
# print(formatted_subjects)
# -----------------------------------------------------------------
# 【ACHV】: Let the user enter "Please enter seconds = ▯", and then convert the seconds into ▯ seconds = ▯ hours ▯ minutes ▯ seconds

# total_seconds= int(input("please enter the number of seconds:"))

# hours = total_seconds //3600
# minutes = (total_seconds % 3600) //60
# seconds = total_seconds % 60

# print (f'{total_seconds}seconds={hours}hours {minutes}minutes {seconds}seconds')
# -----------------------------------------------------------------
# 【ACHV】: Enter minutes, seconds, kilometers, and calculate the runner's average mile per hour speed.

# minutes = float(input("please enter the score:"))
# seconds =float(input("please the number of seconds:"))
# kilometers=float(input("please the number of kilometers:"))

# total_time_hours = minutes / 60 + seconds / 3600

# average_speed_kmh = kilometers / total_time_hours
# average_speed_mph=average_speed_kmh/1.6

# print(f"Average miles per hour:{average_speed_mph} miles per hour")
# -----------------------------------------------------------------
# 【ACHV】: The current time displayed is ▯ hours ▯ minutes ▯ seconds.

# import time

# current_time_seconds = time.time()

# local_time = time.localtime(current_time_seconds + 8 * 3600) # add 8 hours

# hours = local_time.tm_hour
# minutes = local_time.tm_min
# seconds = local_time.tm_sec

# print(f"The current time is {hours}hours {minutes}minutes {seconds}seconds")
# -----------------------------------------------------------------
# 【ACHV】: Conversion time

# seconds = eval (input("please enter the seconds="))

# rMinutes = seconds//60
# rSeconds = seconds % 60
# rHours = rMinutes // 60
# rMinutes2 = rMinutes-rHours*60

# print(seconds,"=",rHours,"hours",rMinutes2,"Minutes",rSeconds,"Seconds")
# -----------------------------------------------------------------
# 【ACHV】: runner
# rMinutes=eval(input("please put in a num of minutes="))
# rSeconds=eval(input("please put in a num of second="))
# rKilometers=eval(input("please put in a num of Kilometers="))

# rMinutes=rSeconds/60+rMinutes
# rHours=rMinutes/60
# rMiles=rKilometers/1.6
# rSpeed=rMiles/rHours

# print("this runner's average miles per hour speed is :", rSpeed)
# -----------------------------------------------------------------
# 【ACHV】: Current Time

# import time
# currentT=time.time()
# totalS = int(currentT)
# totalM = totalS//60
# remainS = totalS%60

# totalH = totalM // 60
# remainM = totalM % 60

# remainH = (totalH + 8) % 24

# print("the current time is", remainH,"hours", remainM,"minutes", remainS,"seconds")

# -----------------------------------------------------------------
# 【ACHV】: the turtle
















































































































