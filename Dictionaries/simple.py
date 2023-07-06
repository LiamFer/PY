
monster_1 = {'type':'orc','life':10}

print(monster_1['type'])

monster_1['guild'] = 'Band of the Hawk'

print(monster_1)

monster2 = {}

monster2['name'] = 'Zodd'
monster2['color'] = 'Black'

print(monster2)

car = {'km':0,'speed':'medium'}

if car['speed'] == 'slow':
    kmAdd = 1
elif car['speed'] == 'medium':
    kmAdd = 2
else:
    kmAdd = 3

car['km'] += kmAdd

del monster2['color']
print(monster2)

for i in monster_1:
    print(monster_1[i])
    

# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

person = {'firstName':'thiago',
          'lastName':'oliveira',
          'age':18,
          'city':'vinhedo',}

for info in person:
    print(person[info])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

fav_numbers = {'thiago':7,
               'eduardo':9,
               'kathleen':3,
               'william':0,
               'matheus':5,}

for info in fav_numbers:
    print(info.title() + " favorite number is " + str(fav_numbers[info]))

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {'list':"We use [] to create a list in Python.",
            'tuple':"We use () to create a tuple in Python.",
            'dictionary':"We use {} to create a dictionary in Python"}

for word in glossary:
    print(word.title() + ':\n' + str(glossary[word]) +'\n')