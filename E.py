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


































































































































