from collections import OrderedDict
from random import randint

# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
# used a standard dictionary to represent a glossary. Rewrite the program using
# the OrderedDict class and make sure the order of the output matches the order
# in which key-value pairs were added to the dictionary.

dictionary = OrderedDict()

dictionary["William"] = 1
dictionary["Thiago"] = 2
dictionary["Eduardo"] = 3

for key,value in dictionary.items():
    print(f"{key} favorite number is {value}")



# 9-14. Dice: The module random contains functions that generate random numbers
# in a variety of ways. The function randint() returns an integer in the
# range you provide. The following code returns a number between 1 and 6:
# from random import randint
# x = randint(1, 6)
# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll
# it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

class dice():
    def __init__(self,sides:int):
        self.sides = sides
    
    def roll(self):
        number = randint(1,self.sides)
        print(number)
        
dado = dice(20)
dado.roll()
        

# 9-15. Python Module of the Week: One excellent resource for exploring the
# Python standard library is a site called Python Module of the Week. Go to
# http://pymotw.com/ and look at the table of contents. Find a module that
# looks interesting to you and read about it, or explore the documentation of
# the collections and random modules.