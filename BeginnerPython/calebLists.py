ages = [12, 18, 28]

people = ["Caleb", "Sabrina", "emily"]

my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]

print(my_favorite_things)
# lists are mutable, unlike strings, strings are immutable cannot be changed. 
# lists can be changed without creating a new one
# see example below

ages = [12, 18, 28]

people = ["Caleb", "Sabrina", "emily"]

my_favorite_things = ["Working out", 7, ['amazon prime', 'netflix']]
print(id(my_favorite_things))
#code above is showing the location in memory

my_favorite_things[0] = "walking"
print(id(my_favorite_things))
#code above is showing the location in memory 

print(my_favorite_things)

print(len(my_favorite_things))

#my_favorite_things = ["working out", 7, ['amazon prime','netflix']]
#copy = my_favorite_things[:]
#print(copy)

#copy[0] = "walking"
#print(my_favorite_things, copy)


my_favorite_things = ["working out", 7, ['amazon prime',['netflix', 'hulu']]]
copy = my_favorite_things.copy()


print(my_favorite_things[2][1][0])


my_favorite_things = ["working out", 7, ["amazon prime", "netflix"]]
least_favorite = ["onions", "goat cheese"]
print(my_favorite_things + least_favorite)

least_favorite = least_favorite + ["editing"]
print(least_favorite)

#lists are mutable 
#strings are immutable