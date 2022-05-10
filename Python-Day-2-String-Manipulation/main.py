# Data Types

#String

print("Hello"[0])
print("Hello"[4])
print("Hello"[-1])

print("123" + "345")

#Integer

print(123 + 345)

#commas interpreted as underscore
123_456_789

#float
3.14159

#Boolean

True
False

############changing types#################
# num_char = len(input("What is your name?"))
# #print("your name has " + num_char + " characters.")
#
# print(type(num_char))
#
# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
#
# print("Your name has " + new_num_char + " characters.")


a = float(123)
print(type(a))
print(70 + float("100.5"))
print(str(70) + str(100))

############Exercise 1 - Data Types#################

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print (int(two_digit_number[0]) +int(two_digit_number[1]))


# PEDMAS ( left to right)
# Parentheses ()
# Exponents **
# Multiplication * # Division /
# Addition + # Subtraction -

print(3 * 3 + 3 / 3 - 3)
#prints 7.0


############Exercise 2 - BMI Calculator#################


# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight) / (float(height)**2)
print(int(bmi))


########number manipulation################
print(round(8 / 3, 2))
print(round(2.666666666, 2))
print(round(8 // 3)) # integer

#f-string
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


############Exercise 3 - Life in Weeks #################

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

left = 90 - int(age)

days = left * 365
weeks = left * 52
months = left * 12

print(f"you have {days} days, {weeks} weeks, and {months} months left.")





