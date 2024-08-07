import math

msg = "Hello"
print(msg)
# \n is an escape character see below for example
msg = "Hello\nHey"
print(msg)
# escape characters are important to format messages or using quotes
# if you want to use an actual \t in your code you would need to use "\\t"
# double quotes and single quotes work the same way in python
# use double quotes for situations like "You're pretty" 
# # another example is when we quote someone, such as "She said \"eww\"" 
# below is concactenation
msg = "you're cute"
msg2 = "hmu"
print(msg + "..." + msg2)
# OR another better way is this
msg = "you're cute"
msg2 = "hmu"
full_message = msg + "..." + msg2
print(full_message)

poem = ("This is all combined"
"as one happy string..."
"what was that sound? "
"it was a doorbell, ring."
" When i see you, my heart sing"
"here plz take this diamond ring")

print(poem)
# the statement above is showing how on the code editor it is on separate lines but in the actual code it is stored as one line 
# now see the statement below if we want to have each sentence on a new line we use triple quotes. see the example below

poem = """This is all combined
as one happy string...
what was that sound? 
it was a doorbell, ring.
When i see you, my heart sing
here plz take this diamond ring"""

print(poem)

poem = "Where am I?"

print(poem)
# index, W is known as number 0, we always start with 0  and you use square brackets to grab the W, 
# spaces are also characters
poem = "Where am I?"

print(poem[1])

# slicing is differnt because you can get a range a characters from string, this is known as slicing 

poem = "Where am I?"

print(poem[:4])
# when using it like this we will get everything up until the 4, which is exclusive
# using the number to the left of the colon is inclusive. 


# using -1 
poem = "Where am I?"

print(poem[-1])

poem = "Where am I?"

print(poem[5:])

poem = "Where am I?"

print(poem[-5:])

task = "Subscribe"
print(id(task))
print(id(task))
print(id(task))
print(id(task))

task = "like"
print(id(task))

# strings are immutable meaning they cannot be changed
# lists support item assignment 

msg = "please subscribe"

print(len(msg))

#msg = "please subscribe"

#print("Your message was " + len(msg) + " characters long")
# you cannot concatenate an intger with a string
# see better example below how to do the above code

msg = "please subscribe"

print("Your message was " + str(len(msg)) + " characters long")

age = 15
print(len(str(id(str(age)) + math.floor(2.6))))


