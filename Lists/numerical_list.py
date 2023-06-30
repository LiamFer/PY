# Making Numerical Lists

# Using the range() Function
# you can use the range() function to print a series of numbers

teste = ['william','thiago','edu']

for i in range(0,len(teste)):
    print(teste[i] + '-' + str(i))
    
numbers = list(range(1,6))
print(numbers)

# We can also use the range() function to tell Python to skip numbers
# in a given range -> range(start,end,step)

print(list(range(1,10,2))) # -> Odd Numbers

times2 = []

for number in range(1,21):
    times2.append(number**2)
    print(times2)
    
print(max(times2))
print(min(times2))
print(sum(times2))

# List Comprehensions
# A list comprehension allows you to generate
# this same list in just one line of code.

times2_list = ['Its '+ str(number**2) for number in range(1,21)]
print(times2_list)

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.

for number in range(1,21):
    print(number)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

# for infinite in range(1,1000000001):
#     print(infinite)

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

million = list(range(1,100001))

print(max(million))
print(min(million))


# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.

for i in range(1,21,2):
    print(i)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

threes = [number*3 for number in range(3,31)]
print(threes)

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cubes = [number ** 3 for number in range(1,11)]
for i in range(0,10):
    print(cubes[i])

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.

cube_comp = [numero ** 3 for numero in range(1,11)]
print(cube_comp)