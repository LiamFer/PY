# Changing, Adding, and Removing Elements

# .append(element) | .insert(index,element)
# del list[index] | .pop() or .pop(index) | .remove(element)

# Modifying Elements in a List

stuff = ['sofa','table','shelf']
stuff[1] = 'bed'
print(stuff)

# Adding Elements to a List

# Appending Elements to the End of a List
stuff.append('table')
print(stuff)
# ['sofa', 'bed', 'shelf', 'table']

# Inserting Elements into a List
# This operation shifts every other value in the list one position to the right:

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1,3)
print(motorcycles)
# ['honda', 3, 'yamaha', 'suzuki']

# Removing Elements from a List

# Removing an Item Using the del Statement
# You can remove an item from any position in a list using the del statement if you know its index.

skywalkers = ['luke','ray','anakin','leia']
del skywalkers[1]
print(skywalkers)
# ['luke', 'anakin', 'leia']

# Removing an Item Using the pop() Method
# The pop() method removes the last item in a list, 
# but it lets you work with that item after removing it.

skywalkers2 = ['luke','ray','anakin','leia']
fake_skywalker = skywalkers2.pop(1)
# Da pra usar o .pop() vazio e ele irá excluir o ultimo elemento da lista,
# Ou podemos usar o .pop(1) com um index de algum elemento para removelo
print (fake_skywalker.title() + " isn't a real Skywalker!")

# Removing an Item by Value
# If you only know the value of the item you want to remove,
# you can use the remove() method.

heroes = ['batman','superman','homelander','midoriya']
print(heroes)
heroes.remove('homelander')
print(heroes)

# You can also use the remove() method to work with 
# a value that’s being removed from a list.

villains = ['all for one','joker','homelander','thanos','ash ketchum']
hero = 'ash ketchum'
villains.remove(hero)
print("\n\t" + hero.title() + " isn't a bad guy.")

# The remove() method deletes only the first occurrence of the value you specify.

# The following exercises are a bit more complex than those in Chapter 2, but
# they give you an opportunity to use lists in all of the ways described.

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

dream_guests = ['nikola tesla', 'friedrich gauss', 'blaise pascal']
print(dream_guests[0].title())
print(dream_guests[1].title())
print(dream_guests[2].title())

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.

print(dream_guests[2].title() + " can't make the dinner!")
dream_guests[2] = 'obiwan kenobi'
print(dream_guests[0].title())
print(dream_guests[1].title())
print(dream_guests[2].title())

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

print("I just happened to find a bigger table folks!")
dream_guests.insert(0,'frodo baggins')
dream_guests.insert(2,'a.-D. sertillanges')
dream_guests.append('marcus aurelius')
print("Guest List -> " + str(dream_guests))
print(dream_guests[0].title())
print(dream_guests[1].title())
print(dream_guests[2].title())
print(dream_guests[3].title())
print(dream_guests[4].title())
print(dream_guests[5].title())

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

print("I can only invite two people for dinner!")
guest6 = dream_guests.pop()
guest5 = dream_guests.pop()
guest4 = dream_guests.pop()
guest3 = dream_guests.pop()

print("I'm sorry " + guest6.title() + " i can't invite you for dinner")
print("I'm sorry " + guest5.title() + " i can't invite you for dinner")
print("I'm sorry " + guest4.title() + " i can't invite you for dinner")
print("I'm sorry " + guest3.title() + " i can't invite you for dinner")

print("Guest List -> " + str(dream_guests))

del dream_guests[1]
del dream_guests[0]

print("Guest List -> " + str(dream_guests))
