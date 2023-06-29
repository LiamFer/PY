# Organizing a List

# Sorting a List Permanently with the sort() Method

names = ['william', 'thiago','eduardo','matheus','ana','kathleen']
# names.sort() -> Organiza em ordem alfabética normal
names.sort(reverse=True) # -> Organiza em ordem alfabética reversa
print(names)

# Sorting a List Temporarily with the sorted() Function
# The sorted() function lets you display your list
# in a particular order but doesn’t affect the actual order of the list.

manga = ['vagabond','berserk','oshi no ko','the climber','monster']

print('This is the original order:\n')
print(manga)

print("\nHere is the sorted list: ")
print(sorted(manga)) 
# The sorted() function can also accept a reverse=True
# argument if you want to display a list in reverse alphabetical order.

# Printing a List in Reverse Order
print(manga)
manga.reverse()
print(manga)

# Finding the Length of a List

manga_length = len(manga)
print(manga_length)

# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

places = ['k2 mountain','everest','canada','waterfalls','grave']
print (places)
print(sorted(places))
print (places)
print(sorted(places,reverse=True))
print (places)
places.reverse()
print (places)
places.reverse()
print (places)
places.sort()
print (places)
places.sort(reverse=True)
print (places)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.

dream_guests = ['nikola tesla', 'friedrich gauss', 'blaise pascal']
print("Im inviting " + str(len(dream_guests)) + " people to dinner.")

# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

stuff = ['k2 mountain','alex honnold']
print(stuff)
stuff.append('vinhedo')
stuff.insert(1,'ryan gosling')
print(stuff)
stuff.remove('vinhedo')
print(sorted(stuff))
stuff.reverse()
print(stuff)
stuff.reverse()
print(stuff)
del stuff[0]
print(stuff)
stuff.insert(0,'rocket league')
print(stuff)
stuff.sort()
print("My stuff list currently has " + str(len(stuff)) + " items.")