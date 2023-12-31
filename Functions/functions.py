
# 8-1. Message: Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.

def display_message():
    print("Im learning something :/")

display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favBook(book):
    print(f"My favorite book is {book.title()}")

favBook("Flowers for algernon")

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size = 'large',text = 'I love Python.'):
    print(f"The {size.upper()} shirt has '{text.title()}' written on it.")

make_shirt(size='medium')

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.

def describe_city(city,country='Brazil'):
    print(f"{city.title()} is in {country.title()}.")
    
describe_city('alagoas')
describe_city('taiwan','china')
describe_city(country='Iceland',city = 'Reykjavik')