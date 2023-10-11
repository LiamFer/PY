current_number = 0
while current_number < 9999:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

topping = ''
while topping != 'quit':
    topping = input("What kind of topping do you want?\n")
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza!")

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

age = ''
while age != 'quit':
    age = int(input("Hi, how old are you?\n---> "))
    if age < 3:
        print("The ticket is completely free for you nano boy.")
    elif age in range(3,13):
        print("The ticket is R$ 10,00")
    else:
        print("The ticket is R$ 15,00")
    


