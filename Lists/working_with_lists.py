# Working with Lists

# Now you’ll learn how to loop through an entire
# list using just a few lines of code regardless of how
# long the list is. Looping allows you to take the same action, or set of actions,
# with every item in a list. As a result, you’ll be able to work efficiently with
# lists of any length, including those with thousands or even millions of items.

jedis = ['luke skywalker','anakin skywalker','obiwan kenobi','yoda','ahsoka tano','windu']

for jedi in jedis:
    print(str(jedis.index(jedi)) + '. ' + jedi.title() + " once was a jedi.\n")
    
print('May the force be with them...\n')

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

pizza_types = ['calabresa','portuguesa','frango']
for pizza in pizza_types:
    print("Eu gosto de pizza de " + pizza.upper())
print('Eu curto pizza demais cara!')

# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!

animals = ['tiger','lion','cheetah']

for animal in animals:
    print("A " + animal.upper() + " would make a great pet.")
print('All these guys could kill you easily')

# Making Numerical Lists