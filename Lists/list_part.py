# Working with Part of a List

# Slicing a List
# As with the range() function, Python stops one item
# before the second index you specify.

jedis = ['luke','anakin','yoda','obiwan','windu','qui-gon','starkiller']
print(jedis[1:4])

# If you omit the first index in a slice, Python automatically starts your
# slice at the beginning of the list

print(jedis[:3])

# A similar syntax works if you want a slice that includes the end of a list.

print(jedis[3:])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])


# Looping Through a Slice

for jedi in jedis[2:-1]:
    print(jedi.upper())

# Copying a List
# To copy a list, you can make a slice that includes the entire original list
# by omitting the first index and the second index ([:]).

people = jedis[:]

jedis.append('Ray')
people.insert(len(people),'Darth Vader')

print("These are my favorite jedis: " + str(jedis))

print("These are my favorite guys: " + str(people))

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# • Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.

print("\tThe first three items in the list are: " + str(jedis[:3]))
print("\tThe first three items from the middle of the list are: " + str(jedis[2:5]))
print("\tThe last three items in the list are: " + str(jedis[-3:]))

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.

pizza_mine = ['calabresa','portuguesa']

pizza_friend = pizza_mine[:]

pizza_friend.append('frango')
pizza_friend.append('barbecue')
pizza_mine.append('chocolate')

print("\n\tMy favorite pizzas are: ")
for pizza in pizza_mine:
    print("\t"+pizza)
    
print("\n\tMy friend's favorite pizzas are: ")
for pizza in pizza_friend:
    print("\t"+pizza)

# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

manga = ['vagabond','berserk','oshi no ko','the climber','monster']

print('\n\tThese are some of the greatest mangas of all time: ')

for index in range(0,len(manga)):
    print("\t" + str(index+1) + '. ' + str(manga[index].title()))