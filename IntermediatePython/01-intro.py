#healthy = ["kale chips", "broccoli"]

#backpack = ["pizza", "frozen custard", "apple crisp", "kale chips" ]

#backpack.remove("pizza")

#print(backpack)

#healthy = ["kale chips", "broccoli"]

#backpack = ["pizza", "frozen custard", "apple crisp", "kale chips" ]

#backpack = [item for item in backpack if item in healthy]

#print(backpack)

    # the above is one way to do it, and the below code will be another way to do it with a loop

#healthy = ["kale chips", "broccoli"]

#backpack = ["pizza", "frozen custard", "apple crisp", "kale chips" ]

#healthy_backpack = []

#for item in backpack:
    #if item in healthy:
        #healthy_backpack.append(item)

#print(healthy_backpack)

squares = []

for i in range(10):
    squares.append(i ** 2)

print(squares)

    #or

sqaures = [i ** 2 for i in range(10)]
print(sqaures)



greetings = ["hi", "hello", "wassup"]
print(greetings[2])

print(len(greetings))

   #or

greetings = ["hi", "hello", "waasup"]

for item in greetings:
    print(item)


backpack = ["sword", "rubber duck", "slice of pizza", "parachute", "sword"]

print(backpack.count("sword"))


#Welcome. We are going to be working through python
#It should be pretty easy to follow along with but if you struggle
#I have a beginner series as well


########## APPEND TO LIST #########


healthy = ["pizza", "frozen custard"]

healthy.append("apple crisp")

print(healthy)


########## CHECKING IF ELEMENT IN LIST #########


#Obviously on our health adventures we want to know if something is healthy.

print("chicken pot pie" in healthy)

#This returns True / False. Can use in keyword within if

backpack = ["pizza", "chicken pot pie", "kale chips"]

if("pizza" in healthy):
    print("eating it")

#We can make this more dynamic. Let's remove pizza from list. 


########## REMOVING FROM LIST ##########


healthy = ["pizza", "frozen custard"]
backpack = ["pizza", "chicken pot pie", "kale chips"]

if("pizza" in healthy):
    backpack.remove("pizza")

print(backpack)


########## LIST COMPREHENSION ##########


healthy = ["kale chips", "broccoli"]
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"] 

backpack[:] = [item for item in backpack if item in healthy]
#slice --> [:] keeps same object id
print(backpack)

#similar to this (except thi one creates new var):
healthy_backpack = []

for item in backpack:
    if item in healthy:
        healthy_backpack.append(item.upper())

print(healthy_backpack)


########## LIST COMPREHENSION ESSENTIALS ##########


squares = [i**2 for i in range(10) if i % 2 == 0]
print(squares)


########## COUNTING ELEMENTS IN LIST ##########

healthy = ["pizza", "frozen custard"]
backpack = ["pizza", "chicken pot pie", "kale chips"]

print(len(healthy), len(backpack))

#You may think of something like healthy.size() or healthy.length() or even healthy.count()
#This is not quite what we are looking for. 
#count is used to count a particular element in a list. Up next!


########## COUNT / CHECK IF ELEMENT EXISTS ##########


print(backpack.count("pizza")) #number of pizza in list

backpack = ["pizza slice", "pizza slice", "pizza slice"]

print(backpack.count("pizza slice")) #3

#This can be used to prevent too many items:
if(backpack.count("pizza slice") < 3):
    backpack.append("pizza slice")
    print("You put a piece of pizza in your backpack")
else:
    print("How about you go to the gym?")


########## INTRO TO SETS ##########


#Don't care about order
#Just need to know yes or no? 
#Sets...

backpack2 = {"sword", "rubber duck", "sice a pizza", "parachute", "sword"}
print("sword" in backpack2)


########## COUNTING WITH LIST COMPREHENSION ##########


backpack = ["sword", "rubber duck", "slice of pizza", "parachute",
"sword", "rubber duck", "slice of pizza", "parachute", 
"sword", "rubber duck", "slice of pizza", "parachute", 
"sword", "rubber duck", "slice of pizza", "parachute",
"cannon", "laser cannon", "Canon 90D", "can of soup"]

counts = [[backpack.count(item), item] for item in set(backpack)]

print(counts)


########## COUNTING ELEMENTS WITH COUNTER ##########

from collections import Counter 
print(Counter(backpack))

