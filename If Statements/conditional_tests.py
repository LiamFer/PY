# Conditional Tests

name = '3'

if name[0] == 'w' or name[0] == 'W':
    print('It starts with w')
elif name[0] == 'm' or name[0] == 'M':
    print('It starts with m')
else:
    print('I dont know')

# Checking for Equality -> ==

print(int(name) == 3) #true

# Ignoring Case When Checking for Equality 

car = 'bmw'

print(car == 'Bmw') #false
print(car.lower() == 'bmw') #true

# Checking for Inequality -> !=

order = 'car'

if order != 'cheese':
    print('Put the cheese away!!')
else:
    print('Its time to eat some cheese!')
    
# Numerical Comparisons -> >= | <= | > | <

age = 111

if age >= 12 and age <=17:
    print("I see you're a teenager")
elif age < 12:
    print("You're a kid!")
else:
    print("You're an adult already!")

# Checking Multiple Conditions -> And | Or

age_1 = 23
age_2 = 34

if (age_1 >= 18) and (age_2 >= 18):
    print('You can get a drivers license already!')
else:
    print('You guys cant drive already!')

# Checking Whether a Value Is in a List -> in

jedis = ['luke','anakin','yoda','obiwan','windu','qui-gon','starkiller','ray']

if 'ray' in jedis:
    print("Something is wrong")
else:
    print("Yah that's alright")

# Checking Whether a Value Is Not in a List -> not in

jedis.remove('ray')

if 'ray' not in jedis:
    print("Now everything is fine as it should be...")

test = True

if test:
    print('it works')


# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

fruit = 'banana'

if fruit == 'apple':
    print('Yes its an apple')
elif fruit == 'banana':
    print('Its a banana!')
elif fruit == 'orange':
    print('Its an orange')
else:
    print('I have no idea of what this thing is')


# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() function
# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

array = [number * 2 for number in range(1,21)]
print(array)

if 2 in array:
    print('Yes the array has the number 2')

if 100 not in array:
    print('No we dont have the number 100 inside our array.')

if (10 in array) and (36 in array):
    print('The array has the numbers: 10, 36')
    
if array[0] <= array[1]:
    print (str(array[0]) + " is lesser than " + str(array[1]))





