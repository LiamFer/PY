# Looping Through All Key-Value Pairs

user_0 = {"username":'gauss',
          "first":"friedrich",
          "last":"oppenheimer"}

print(user_0.items())

for key,value in user_0.items():
    print(key)
    print(value)
    
favorite_languages = {'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name,language in favorite_languages.items():
    print(name.title() + " favorite programming language is " + language)
    
# Looping Through All the Keys in a Dictionary
friends = ['edward','sarah']

for key in favorite_languages.keys():
    print(key.title())
    if key in friends:
        print("Sup " + key.title() + " i see your favorite language is " + favorite_languages[key].title())
        
# Looping Through a Dictionary’s Keys in Order
# We need to use the sorted() method:

for key in sorted(favorite_languages.keys()):
    print(key.upper())
    
# Looping Through All Values in a Dictionary

languages = []
for value in favorite_languages.values():
    if value not in languages:
        languages.append(value)
        print(value)
    
# When you wrap set() around a list that contains duplicate items, Python
# identifies the unique items in the list and builds a set from those items.

for value in set(favorite_languages.values()):
    print(value.upper())
    
# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

python_terms = {1:"set()",
                2:"items()",
                3:"values()",
                4:"keys()",
                5:"sorted()"}

for term in python_terms.keys():
    print(term)

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {"nile":'egypt',
          "eufrates":"egypt",
          "tietê":"brasil"}

for river,country in rivers.items():
    print("The " + river.title() + " runs through " + country.title())

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

poll = {'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'william':'javascript',
'thiago':"sql",
"matheus":"python"}

people = ['daniel','dionizio']

for person in poll.keys():
    if person not in people:
        print(person.title() + ' thank you!')
    else:
        print(person.title() + ' you should take the poll!')