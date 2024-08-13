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

