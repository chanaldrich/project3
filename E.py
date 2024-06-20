# len,find,capitalize,upper,lower

# name ="pro gamer B)"
# length =len(name)
# print("your full name have",length,"in it.")

# space_pos=name.find(" ")
# print("your first space is on",space_pos)

# name_capitalized=name.capitalize()
# print("your full name(first letter capital)",name_capitalized)

# name_upper=name.upper()
# print("your full name(all letter capital)",name_upper)

# name_lower=name.lower()
# print("your full name(all letter capital)",name_lower)
# -------------------------------------------------------------------------------
# count,replace

# phone_number = input("put in your phone number:")
# dash_count =phone_number.count("-")
# print("your phone number has",dash_count,"dash in it")

# phone_number = phone_number.replace("-"," ")
# print("your phone number",phone_number)
# -------------------------------------------------------------------------------
# username with only english letters and less then 12 letters and no spaces

# username=input("please put in your new username:")

# if len(username) >12:
#     print("you can't have more then 12 letters")
# elif " " in username:
#     print("you can't have any spaces in your username")
# elif not username.isalpha():
#     print("your username can only have english letters in it")
# else:
#     print('welcome '+username)
# -------------------------------------------------------------------------------
# string index

# credit_number="1234-5678-95031"

# first_char=credit_number[0]
# print("first char:",first_char)

# second_char=credit_number[1]
# print("second char:",second_char)

# first_four= credit_number[0:4]
# print("first four char:",first_four)

# last_one=credit_number[-1]
# print("last char:",last_one)

# last_two=credit_number[-2]
# print("last 2 char:",last_two)
# -------------------------------------------------------------------------------
#email string analysis

# email="aldrichpu@gmail.com"
# index=email.index("@")
# print(index)
# print(email[:index])
# print(email[(index+1):])
# -------------------------------------------------------------------------------
# f-string formatted string

# price_1=3.1415
# price_2=-69
# price_3=22.83
# print(f"price 1 is {price_1:.2f}\n"
#       f"price 2 is {price_2:.2f}\n"
#       f"price 3 is {price_3:.2f}")
# print(f"price 1 is {price_1:+.2f}\n"
#       f"price 2 is {price_2:+.2f}\n"
#       f"price 3 is {price_3:+.2f}")
# print(f"price 1 is {price_1:^10.2f}\n"
#       f"price 2 is {price_2:^10.2f}\n"
#       f"price 3 is {price_3:^10.2f}")
# print(f"price 1 is {price_1:>+.2f}\n"
#       f"price 2 is {price_2:>+.2f}\n"
#       f"price 3 is {price_3:>+.2f}")
# -------------------------------------------------------------------------------
# while loop

# name = ""
# while name == "":
#     name = input("please put in your name :")
# print(f"hi {name}!")

# food=input("put in the food that you likes :")
# while food != "q":
#     print(f"the food that you likes is {food}")
#     food=input("put in the food that you likes :")
# print("bye!")

# num = int(input("plz put in number 1 to 10 :"))
# while num < 1 or num >10:
#     print(f"the number you typed {num} can't work")
#     num = int(input("plz put in number 1 to 10 :"))
# print(f"you typed {num}.")
# -------------------------------------------------------------------------------
# compound interest computer

# amount = 0
# rate = 0
# time = 0
# while amount <= 0:
#     amount = float(input("please enter the principal amount :"))
#     if amount <= 0:
#         print("the principal amount cannot be small or equal to 0")



# while rate <= 0:
#     rate = float(input("put in a interest rate :"))
#     if rate <= 0:
#         print ("rate can't be smaller tor equal to 0")



# while time <= 0:
#     time = int(input("put in a time(years) :"))
#     if time <= 0:
#         print ("time can't be smaller tor equal to 0")
# print("amount :",amount)
# print("rate :",rate)
# print("years:",time)

# total = amount * (1+ (rate/100)) ** time
# print ("total :",total)
# -------------------------------------------------------------------------------
# for loop

# for x in range(1, 11):
#     print(x)

# for x in reversed(range(1, 11)):
#     print(x)
# print("happy new year!!")

# credit_card ="1234-5678-9012-3456"
# for x in credit_card:
#     if x == "9":
#         continue
#         break
#     else:
#         print(x)

# my_dict = {"a": 1, "b": 2, "c": 3}
# for x in my_dict:
#     print(x)
# for key, value in my_dict.items():
#     print("key:", key)
#     print("value:", value)
# -------------------------------------------------------------------------------
# nested loop

# for x in range(1, 10):
#     print(x, end=" ")

# for y in range(5):
#     for x in range(1, 10):
#         print(x, end=" ")
#     print()

# rows = int (input("Please enter the number of rows:"))
# cols = int (input("please enter the number of cols:"))
# symbol = input("please enter the symbol:")

# for i in range(rows):
#     for j in range (cols):
#         print(symbol, end=" ")
#     print()
# -------------------------------------------------------------------------------
# stopwatch

# import time
# my_time= int(input("please enter seconds:"))
# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = x // 60 % 60
#     print(f"{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("the time is up!")
# -------------------------------------------------------------------------------
# list,sets,tuple

# list

# fruits=["apple","orange","banana","cocoNUT"]

# print(fruits[1])

# for f in fruits:
#     print(f)

# fruits.append("Guava")
# print(fruits)

# fruits.remove("cocoNUT")
# print(fruits)

# print(fruits.index("banana"))
# fruits.append("apple")
# fruits.append("apple")
# print(fruits)

# print(fruits.count("apple"))

# print(fruits)
# fruits.reverse()
# print(fruits)
# ----------------
# set

# fruit_set ={"🍎","🍊","🍌"}
# fruit_set.add("🍎")
# fruit_set.add("🍉")
# for fruit in fruit_set:
#     print(fruit, end=" ")
# if "🍎" in fruit_set:
#     print("an apple.")
# if "🍉" in fruit_set:
#     print("a watermelon.")
# else:
#     print("no watermelon...=(")
# ----------------
# tuple

# fruits_tuple = ("🍎","🍊","🍌","🍎")
# result = fruits_tuple.count("🍎")
# print(result)
# result = fruits_tuple.index("🍊")
# print(result)

# fruits_tuple.add("🍎") #can't use
# -------------------------------------------------------------------------------
# shopping cart program (list, set, tuple)

# goods = []
# prices = []

# while True:
#     good = input("please enter things you want to buy :")
#     if good.lower() == "q":
#         break
#     price = float(input(f"please enter {good}'s price : "))
#     goods.append(good)
#     prices.append(price)
# print("Product list:", goods)
# print("price list :", prices)
# for index, good in enumerate(goods):
#     print(f"Item {index + 1} is {good},price:{prices[index]:.2f}")

# total = sum(prices)
# print(f"total cost: ${total}")
# -------------------------------------------------------------------------------
# Dictionary

# capital = {
#     "United States": "Washington DC",
#     "Japan": "Tokyo",
#     "France": "Paris",
#     "Russia": "Moscow"
# }

# print(capital.get("Japan"))
# print(capital.get("France"))

# capital.update({"Gemany": "Berlin"})
# print(capital)

# capital.pop("United States")
# print(capital)

# print(capital.values())

# print(capital.items())
# -------------------------------------------------------------------------------
# vending machine program

# menu={
#     "pizza":100,
#     "popcorn":50,
#     "franch fries":30,
#     "potato chips":40,
#     "soft breadsticks":50,
#     "soda":40,
#     "lemonade":50
# }
# print("menu")
# print("----------")
# cart = []
# total = 0
# for item, price in menu.items():
#     print(f"{item}:{price}")
# while True:
#     food=input("please enter a food that's in the menu(enter q to quit):")
#     if food == "q":
#         break
#     elif menu.get(food) is None:
#         print(f"there's no {food} in this menu")
#     else:
#         cart.append(food)
#         total += menu.get(food)
#         print(food, end=" ")
# print(f"the total is: {total}")
# -------------------------------------------------------------------------------
# Number guessing game (using random)

# import random

# print(random.randint(1,10))

# print(random.random())

# options = ["rock","paper","scissors"]
# rand_option = random.choice(options)
# print("the computer choose:", rand_option)

# cards=["2","3","4","5","7","8","9","10","A","B","C","D"]
# random.shuffle(cards)
# print(cards)
#-------------
# game :

# low=1 
# high=10000
# num=random.randint(low,high)
# guesses=0

# while True:
#     guess = int(input(f"please enter a num between {low} ~ {high}:"))
#     guesses += 1
#     if guess < num :
#         print("guessed number is too low")
#     elif guess > num:
#         print("guessed number is too high")
#     else:
#         print(f"Congratulations! the number is {num}!")
#         print (f"you guessed {guesses} times.")
#         break
# -------------------------------------------------------------------------------
# dice program

# import random

# dice_art = {
#     1: (
#         "┌───────┐",
#         "│       │",
#         "│   ●   │",
#         "│       │",
#         "└───────┘"
#     ),
#     2: (
#         "┌───────┐",
#         "│ ●     │",
#         "│       │",
#         "│     ● │",
#         "└───────┘"
#     ),
#     3: (
#         "┌───────┐",
#         "│ ●     │",
#         "│   ●   │",
#         "│     ● │",
#         "└───────┘"
#     ),
#     4: (
#         "┌───────┐",
#         "│ ●   ● │",
#         "│       │",
#         "│ ●   ● │",
#         "└───────┘"
#     ),
#     5: (
#         "┌───────┐",
#         "│ ●   ● │",
#         "│   ●   │",
#         "│ ●   ● │",
#         "└───────┘"
#     ),
#     6: (
#         "┌───────┐",
#         "│ ●   ● │",
#         "│ ●   ● │",
#         "│ ●   ● │",
#         "└───────┘"
#     )
# }
# # print(dice_art.get(6))
# num_dice = int(input("Please enter how many dice you want to roll:"))
# dice = []
# for i in range(num_dice):
#     dice_number = random.randint(1,6)
#     dice.append(dice_number)
# print(dice)

# def get_dice_number(number):
#      for i in range(5):
#         print(dice_art.get(number)[i])
# for i in dice:
#     get_dice_number(i)
# print("sum:",sum(dice))
# only 10 dices:
# highest :47 
# lowest:22
# -------------------------------------------------------------------------------
# function (program)

# def say_hello():
#     print("hello world!")
# say_hello()
# say_hello()
# say_hello()

# def greeting(name):
#     print(f"greetings! {name}!")
# greeting("aldrich")

# def add(x, y):
#     return x + y

# result=add(3, 5)
# print(result)

# def sub(x, y):
#     return x - y

# result2=sub(5, 2)
# print(result2)

# def mul(x, y):
#     return x * y

# result3=mul(2, 7)
# print(result3)

# def devide(x, y):
#     return x / y

# result4=devide(15, 3)
# print(result4)

# def creat_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last
# print (creat_name("chan","aldrich"))
# -------------------------------------------------------------------------------
# function(number)

# def greet(name, greeting="hello"):
#     print(f"{greeting},{name}")
# greet("aldrich", "hi")
# greet("chan")
# -------------------------------------------------------------------------------
# rock paper scissors game

#  these code rn in not done for good, so can't use it
#  all of these are weird,and idk how to fix it,maybe when i am better at python i will fix this

# import random
# player=None
# computer=None
# options=("rock","paper","scissors")
# running=True
# while running:
#     player = input("enter rock,paper or scissors:")
#     while player not in options:
#         input("can't put that.enter rock,paper or scissors:")
#     computer= random.choice(options)
#     print (f"player:{player},computer:{computer}")
#     if player == computer:
#        print ("tie") 
#     elif player == "scissors"and computer == "paper":
#         print("player wins")
#     elif player == "rock"and computer == "scissors":
#         print("player wins")
#     elif player == "paper"and computer == "rock":
#         print("player wins")
#     else:
#         print("computer won")
#     play_again=input("play again?(y/n)").lower()
#     if not play_again == "y":
#         running=False
    
# print("thx for playing")
# -------------------------------------------------------------------------------
# Keyword arguments

# def hello(greeting, title, first_name, last_name):
#     print(f"{greeting},{title}, {first_name}, {last_name}")

# hello("hi!", "Mr", "Chan", "aldirch")
# hello(greeting="hi!",title="Mr",first_name="Chan",last_name="aldirch")

# def get_phone(country_code, area_code, first, last):
#     return f"{country_code}-{area_code}-{first}-{last}"
# str=get_phone(country_code="123",area_code="45",first="6789",last="0123" )
# print(str)
# -------------------------------------------------------------------------------
# Args and Kwargs 

# def add(a, b):
#     return a+b
# print(add(1,2))

# def add(*args):
#     total = 0
#     for arg in args:
#         print(f"arg: {arg}")
#         total+=arg
#     return total
# print(add(1,2,3))

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"key: {key}, value: {value}")
# print_info(name="Aldrich", age="12", occupation="none")
# -------------------------------------------------------------------------------
# Modules

# import my_module as m
# print(m.area(5))

# import math as m
# from math import pi
# print(pi)
# help(math)

# print(m.pi)
# print(m.pow(3,2))
# print(m.pow(3,3))

# num = 20.6
# print(m.ceil(num))
# print(m.floor(num))
# print(round(num))
# -------------------------------------------------------------------------------
# Scope

# a = 10
# def function_one():
#     a=1
#     print("a=",a)
#     def function_two():
#         b=2
#         print("b=",b)    
#         print("a=",a)
#     function_two()
# function_one()

# from math import e
# print(e)
# print (round(e))

# def function_one():
#     print(e)
# function_one
# -------------------------------------------------------------------------------
# Exception handling 

# try:
#     x = int(input("please enter a integer:"))
#     y = int(input("please enter another integer:"))
#     print(x/y)
# except ValueError:
#     print("please enter a integer")
# except ZeroDivisionError:
#     print("The divisor cannot be zero")
# except (ValueError,ZeroDivisionError):
#     print("ERROR,please put another one!")
# else:
#     print("else")
# finally:
#     print("will always do the things even tho they are not right")
# -------------------------------------------------------------------------------
# Check if the file exists

# import os

# str = r"c:\Users\HAPU\Desktop\project3\test.txt"
# print(str)
# if os.path.isfile(str):
#     print("the path is file.")
# elif os.path.isdir(str):
#     print("the pathis dir.")
# else:
#     print("other")
# -------------------------------------------------------------------------------
# Read file

# i used other file cuz i cant do this one(c:\Users\HAPU\Desktop\project3)
# str=r"c:\Users\HAPU\Desktop\hi\hi.txt"
# try:
#     with open(str) as file:
#         print(file.read())
# except FileNotFoundError:
#     print("file is not real")
# -------------------------------------------------------------------------------
# 




















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































