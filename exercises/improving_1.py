# For loops

# Make a program that lists the countries in the set

clist = ['Canada','USA','Mexico','Australia']

for country in clist:
    print(country)
    
# Create a loop that counts from 0 to 100

store = ''
for number in range(0,101):
    store += "\n\t" + str(number)
print(store)

# Make a multiplication table using a loop

for number in range(1,11):
    equation = '| ' + str(number) + ' * ' + '2 ' + '= ' + str(number*2) + ' |'
    upperscores = '‾'
    underscore = '_'
    for i in range(1,len(equation)):
        underscore += '_'
    print(underscore)
    for size in range(1,len(equation)):
        upperscores += '‾'
    print(equation)
    print(upperscores)

# Output the numbers 1 to 10 backwards using a loop

numbers = [number for number in range(1,11)]
numbers.reverse()
for number in numbers:
    print(number)
    
# Or

numeros = [numero for numero in range(1,11)]
print(numeros)

for i in range(1,len(numeros)+1):
    index = '-'+ str(i)
    if index != '-0':
        print(numeros[int(index)])
    else:
        print(numeros[0])

# Create a loop that counts all even numbers to 10

for number in range (1,10,2):
    print(number)
    
# Create a loop that sums the numbers from 100 to 200

charge = 0
for number in range(100,201):
    charge += number
print(charge)

# If statements

# Make a program that asks the number between 1 and 10. If the number is out of range the program should display “invalid number”.

input_number = int(input("\n\tType a number between 1 and 10: "))

if input_number in range(1,11):
    print('Its right')
else:
    print("That's an invalid number!")

# Make a program that asks a password.

input_password = input("\n\n\tType your password: ")

