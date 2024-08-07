import math

print("hello world")
print(5+ 5)
age = 5
print(age)
# the hashtag sign is also for comments in python 
# leaving notes and explanations for how code works 
# always leave notes 
# python does not have a multiline comment like other languages does but there is a way around it, using 3 double qoute """
# naming variables have rules, also use names that make sense.
# age1 as variable is ok
# age_2 as a variable is valid
# age_of_user as a variable is valid, and using underscores to name is a common convention for python unlike camelCase, 
# age-3 is NOT valid, you cannot you hypens in variable names only underscores
# 4age is NOT valid, you cannot start a variable with a number. 
# Age is NOT valid, it is allowed but NOT recommended, do not start with uppercase
# return is NOT valid, bc it is a word for python. 

result = 10//3

#print(math.floor(result))
# / one division --> float division
# // two divisions --> integer division (math.floor)

print(result)

# modulus operator will give you the remainder of some division. 
# example would be 10/3 which would be 3 goes into 10 3 times with 1 left over, 
# 10 % 3 would return 1 for modulus 
# another example is number = 345345   
# limit = 10
# print(number % limit)  the modulus would be 5 

number = 345345
limit = 10
print(number % limit )

result = math.pow(3, 5)
print(result)

#variables are used bc we don't want to type out the value of something 10 times or 20 times, and instead using a variable will only need to change in 1 place.
# Variables prevents us from having to change code in tons of places.
# we also won't always know the value of something, so therefore variables are used for that reason too. A value can come from user input, or database, or some other form.
# variables prevent repeating values and makes vode more readable. 
