#workdays = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

#print(workdays[3])

#workdays.insert(2, "Wednesday")

#print(workdays[3])

#print(workdays)


    #taking days out

#workdays.remove("Saturday")
#print(workdays)

    # Or remove using del method

    # or remove using pop method 


workdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

del workdays[-1]

print(workdays)


backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "sandwich from mcdonalds"]

backpack.remove("pizza slice")
print(backpack)

while backpack.count("pizza slice") > 0:
    backpack.remove("pizza slice")

print(backpack)


    #or better solution to go through each item in the list


data = [0, 1, 2, 3, 4, 5, [1, 2, 3,]]

data.reverse()

print(data)



