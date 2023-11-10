
class person():
    
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
    
    def walk(self):
        print(f'{self.name.title()} is walking right now!')
        

marcio = person("Thiago",18)

marcio.walk()

# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class restaurant():
    def __init__(self,restaurant_name:str,cuisine_type:str):
        self.name = restaurant_name
        self.type = cuisine_type
        self.served = 0

    def set_served(self,clients:int):
        self.served = clients
        
    def add_served(self,clients:int):
        self.served += clients
    
    def describe_restaurant(self):
        print(f"The restaurant name is {self.name.title()} and it's cuisine type is {self.type.title()}")
    
    def open_restaurant(self):
        print(f"{self.name.title()} is open now!")
        
restaurante = restaurant("Los polos Hermanos","Crystal Meth")
print(f"{restaurante.name} cooks {restaurante.type}")
restaurante.describe_restaurant()
restaurante.open_restaurant()

# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class user():
    
    def __init__(self,name:str,password:str,location:str):
        self.name = name
        self.password = password
        self.location = location
        self.tries = 0
    
    def login(self):
        self.tries += 1
        
    def reset_login(self):
        self.tries = 0
    
    def infos(self):
        infos = {"name":self.name.title(),"password":self.password,"location":self.location.title()}
    
    def compare(self,user):
        # You can use __dict__ to transform an object to a dictionary
        for attr, value in user.__dict__.items():
            if value == self.name:
                print("They have the same name!")
            print(attr, value)
        
william = user("william","123456","brazil")

william.compare(william)

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.

restaurante.served = 10

restaurante.add_served(150)
restaurante.set_served(20)
print(restaurante.served)



# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

william.login()
william.login()
william.login()
william.login()
william.login()
william.login()
william.login()
william.reset_login()
print(william.tries)

class user2(user):
    
    def __init__(self, name: str, password: str, location: str):
        super().__init__(name, password, location)
    
    def compare(self):
        print("Give up bro")

gauss = user2("Gauss","98765","Norway")

gauss.compare()
      
