def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',a='princeton',field='physics',area="vinhedo")
print(user_profile)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that is being ordered. Call the function three times, using a different number
# of arguments each time.

def sandwiches(*sandwichs):
    print('You ordered:\n')
    for sandwich in sandwichs:
        print(sandwich)  

sandwiches("pizza",'brick','tower','flip flops')


# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.

def make_car(manufacturer:str,model:str,**plus_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key,value in plus_info.items():
        car[key] = value
    print(car)
    return car

make_car('subarro','outback',color='black',nitro=True,year=1982,speed=220)