# Introducing Lists

characters = ['boromir','aragorn','legolas','frodo']
print (characters[-1].title())

# Using Individual Values from a List

print('My favorite character from Lord of the Rings is ' + characters[1].title())

# Try these short programs to get some firsthand experience with Python’s lists.
# You might want to create a new folder for each chapter’s exercises to keep
# them organized.

# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.

friends = ['thiago','eduardo','kathleen','matheus']
print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name.

print('Hello ' + friends[0].title() + ", you're in the index " + str(0))
print('Hello ' + friends[1].title() + ", you're in the index " + str(1))
print('Hello ' + friends[2].title() + ", you're in the index " + str(2))
print('Hello ' + friends[3].title() + ", you're in the index " + str(3))

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

transportation_modes = ['car','airplane','boat','train','motorcycle']

print('I would like to own a ' + transportation_modes[0])
print('I would like to own a ' + transportation_modes[1])
print('I would like to own a ' + transportation_modes[2])
print('I would like to own a ' + transportation_modes[3])
print('I would like to own a ' + transportation_modes[4])
