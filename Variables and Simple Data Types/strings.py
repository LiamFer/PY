
name = 'marcus aurelius'

# Methods
print(name.title())
print(name.upper())
print(name.lower())

# Combining or Concatenating Strings

first_name = 'aditya'
middle_name = 'y.'
last_name = 'bhargava'
full_name = first_name.title() + ' ' + middle_name.upper() + ' ' + last_name.title()
print(full_name)

message = '\tHello, ' + full_name + '!'
print(message)

# Adding Whitespace to Strings with Tabs or Newlines

# \t -> Adds a Tab
# \n -> Adds a New Line

print('Greatest Mangas of all time:\n\tVagabond\n\tBerserk\n\tVinland\n\tThe Climber')

# Stripping Whitespace

# .lstrip() -> Removes the Whitespace from the left
# .rstrip() -> Removes the Whitespace from the right
# .strio() -> Removes the Whitespace from both sides (It seems to be more useful ngl)

favorite_manga = ' the climber '
favorite_manga2 = 'the climber'
print(favorite_manga.strip())
print(favorite_manga.strip() == favorite_manga2)

# Save each of the following exercises as a separate file with a name like
# name_cases.py. If you get stuck, take a break or see the suggestions in
# Appendix C.

# 2-3. Personal Message: Store a person’s name in a variable, and print a message
# to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

guy_name = ' mori buntarou'
friends_name = guy_name.strip()
guy_name = guy_name.title()
print("Let's Climb " + guy_name)

# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s
# name in lowercase, uppercase, and titlecase.

warrior_name = ' miyamoto musashi'
warrior_name = warrior_name.lstrip()
print(warrior_name.lower())
print(warrior_name.upper())
print(warrior_name.title())


# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a
# mistake never tried anything new.”

author = 'seneca '
author = author.rstrip()
print('\t' + author.title() + ' once said, "We suffer more often\n\tin imagination than in reality."')

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s
# name in a variable called famous_person. Then compose your message
# and store it in a new variable called message. Print your message.

author2 = ' marcus aurelius '
author2 = author2.strip()
author_quote = 'The best revenge\n\tis not to be like your enemy.'
print('\t' + author2.title() + " once said," + '"' + author_quote + '"')

# 2-7. Stripping Names: Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

person_name = '\n\t Gauss '
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())