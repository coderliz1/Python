#healthy = ["kale chips", "broccoli"]

#backpack = ["pizza", "frozen custard", "apple crisp", "kale chips" ]

#backpack.remove("pizza")

#print(backpack)

healthy = ["kale chips", "broccoli"]

backpack = ["pizza", "frozen custard", "apple crisp", "kale chips" ]

backpack = [item for item in backpack if item in healthy]

print(backpack)