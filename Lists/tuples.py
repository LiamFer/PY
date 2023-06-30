# Tuples
# Sometimes you’ll want to create a list of items that cannot
# change. Tuples allow you to do just that.

size = (100,300)

for dimension in size:
    print(dimension)
    
print(size)

# Writing over a Tuple
# Although you can’t modify a tuple, you can assign a new value to a variable
# that holds a tuple.

size = (400,500,600)
print(size)
for dimension in size:
    print(dimension)

# When compared with lists, tuples are simple data structures. Use them
# when you want to store a set of values that should not be changed throughout
# the life of a program.

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

buffet = ('baby beef','alcatra','picanha','pão de alho','linguiça')
print("\n\tToday the restaurant is offering: \n")
for food in buffet:
    print("\t" + str(food))



buffet = ('ovo cozido','fabitos','picanha','pão de alho','salsicha')
print("\n\tTomorrow the restaurant will offer: \n")
for food in buffet:
    print("\t" + str(food))
