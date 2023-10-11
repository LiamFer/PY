
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')
#     print(pets)
    

# dct = {}
# i = 0
# people = int(input("How many people are you going to ask these questions?\n---> "))
# while i < people:
#     personName = input("What is your name?\n---> ")
#     personAnswer = input("What's your favorite song?")
#     dct[personName] = personAnswer
#     i+=1

# print(dct.items())

# for name,answer in dct.items():
#     print(f"{name.title()} favorite song is {answer}!")

# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
orders = ['atum','pastrami','pizza','pepperoni','pastrami','sausage','pastrami']
done = []

print('Sorry today we dont have enough pastrami!')
while 'pastrami' in orders:
    orders.remove('pastrami')

print (orders)

while orders:
    sandwich = orders.pop()
    print(f"I just finished making your {sandwich} sandwich!")
    done.append(sandwich)
    

print(orders)
print(done)

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.




# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.