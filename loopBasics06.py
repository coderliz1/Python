#friends = ["abby", "jon", "becky", "Ryan"]

#for friend in friends:
    #print(friend, end=" ")
#print()

#for i in range(10):
    #print(i)

    #code above is how many iterations of the loop, this will output 9 bc it is 0 to 9 which is 10, now if you don't want to include the 0 then you will modify the code in the print
    #statement so it would be i + 1 instead of just i



for i in range(231, 501, 2):
    print(i, end=" ")
print()


sum = 0

for i in range(10):
    print(i)
    sum += i

print(sum)


# Calebs code below
#Once you understand logic, you can apply the same principles to looping

languages = ["Python", "C++", "Java"]

for x in languages:
    print(x)

#The body of this loop (the indented part) will run 4 times
#Each time is known as an iteration
#Each iteration, the variable x will contain one element
#iteration 1 will be the first element
#iteration 2 will be the next, and so on.
#The loop automatically stops. 

#The variable name is irrelevant
for language in languages:
    print(language)


########## PRINT WITHOUT NEWLINE ##########

print("One", end=" ")
print("Line")

#This is useful for loops where you don't want to spam the terminal
for language in languages:
    print(language, end =" ")
print()
#can end with newline tfor future prints

#You could alternatively use end="\t" or end="" or whatever you want.

#You might be confused why we have to put end and not just:
print("DOEN'T AFFECT END", " ")

#Because this is interpretted as a second argument to print
#resulting in a printed " " followed by a newline.
#We must use end= (This is an example of keyword argument)


########## RANGE FUNCTION ##########


#instead of iterating through a list, we can use a function called range
#This loop runs 10 times
for i in range(10):
    print("loading...", end= " ")
print()

#i is known as in iteration variable
#i will obtain a value each iteration based on the range we select. 
#for range(10), we get 0-9:

for i in range(10):
    print(i, end=" ")
print() 

#Important: the value to end at is never part of the range. 
#With range(10) we get 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


########## RANGE START POSITION ##########


#We can count 1-10 instead of 0-9 if desired:
for i in range (1, 11):
    print(i, end=" ")
print()

#We can start anywhere and end anywhere
for i in range (5, 7):
    print(i, end=" ")
print()


########## RANGE STEP ##########


#Go the other way. 
#9 included. -1 not included (result is 9-0)
for i in range (9, -1, -1):
    print(i, end=" ")
print()

#The third argument is called the step. we can set it to whatever
#Count down from 100 to 0, by 10s.
for i in range (100, -1, -10):
    print(i, end=" ")
print()

########## SUM OF LIST ##########

#https://docs.python.org/3/library/math.html
#methods taking an iterable can take a range (sum, prod)

#Sum of numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#print(sum(range(1, 11)))  <----- showing an error


########## LIST FROM RANGE ##########

#We can make the range an official list using the list ctor
#https://docs.python.org/3/library/stdtypes.html#list
numbers = list(range(1, 11))
print(numbers)

#This is the besr way to easily print a list 
#as print(range(1,11)) doesn't work as expected

########## FOR LOOP WITH INDEX ##########
 
languages = ["Python", "C++", "Java"]
for i in range(len(languages)):
    print(i, languages[i])

#len will return 3. Passing 3 to range gives us 0, 1, 2