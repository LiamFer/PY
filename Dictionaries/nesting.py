# Nesting

# A List of Dictionaries

jedi_0 = {'first':"obiwan",'last':"kenobi"}
jedi_1 = {'first':"luke",'last':"skywalker"}
jedi_2 = {'first':"anakin",'last':"skywalker"}


jedis = [jedi_0,jedi_1,jedi_2]

for jedi in jedis:
    print(jedi)
    
aliens = []

for alien in range(30):
    new_alien = {'speed': 'slow', 'color': 'green', 'points': 5}
    aliens.append(new_alien)

for alien in aliens[:7]:
    print(alien)

for alien in aliens[3:7]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'
        
for alien in aliens[:7]:
    print(alien)

print(len(aliens))

pizza = {'crust':"thick",
         "toppings":['mushrooms','extra cheese']}

print("\nYou ordered a " + pizza['crust'] + "-crust pizza\nwith the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
    
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for person,languages in favorite_languages.items():
    print(person.title() + "'s favorite languages are:")
    for language in languages:
        print(language.title())
        
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}

for username, infos in users.items():
    fullname = infos['first'].title() + ' ' + infos['last'].title()
    print("The user -> " + username.title())
    print("Also known as " + fullname + " used to live in " + infos['location'].title() + '.')

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
# Dictionaries 115

person_0 = {'first':'thiago','last':"oliveira",'likes':"anime"}
person_1 = {'first':'william','last':"fernandes",'likes':"manga"}
person_2 = {'first':'eduardo','last':"dornellas",'likes':"fifa"}

people = [person_0,person_1,person_2]

for person in people:
    fullname = person['first'] + ' ' + person['last']
    print(fullname.title() + " likes " + person['likes'].title())

# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.

pet0 = {'name':"barney","kind":"doggo","owner":"william"}
pet1 = {'name':"maylon","kind":"doggo","owner":"eduardo"}
pet2 = {'name':"agatha","kind":"cat","owner":"thiago"}

pets = [pet0,pet1,pet2]

for animal in pets:
    print("The pet name is " + animal['name'].title() + " and it's a " + animal['kind'].title() + " it's owner is " + animal['owner'].title())


# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_numbers = {
    "william":[7,1],
    "thiago":[2],
    "kathleen":[3,9]
}

for person,numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(person.title() + "'s favorite number is " + str(numbers[0]))
    else:
        print(person.title() + "'s favorite numbers are:")
        for number in numbers:
            print(number)
    

# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

cities = {
    "vinhedo":{"country":"brazil","population":80000,"fact":"I was born there!"},
    "sumaré":{"country":"brazil","population":90000,"fact":"I have a brother there."},
    "pindamonhangaba":{"country":"brazil","population":7500000,"fact":"Jordan were born there"},
}

for city, infos in cities.items():
    print("City: " + city.title())
    information = "About: "
    for key,value in infos.items():
        valor = str(value)
        if value is str:
            valor = value.title()
        information += "\n\t" + key.title() + ': ' +valor
    print(information)
    
