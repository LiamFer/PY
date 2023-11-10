# Classes que criei anteriormente

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

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method. 

class iceCreamStand(restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str,*flavors:str):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def show_menu(self):
        print("\nCurrently we have these flavors:\n")
        for flavor in self.flavors:
            print(f"- {flavor}")
        print("\n")
sorvataria = iceCreamStand("Sergel","Ice Cream","Chocolate","Strawberry","Mango","Kit Kat","Nutella")

sorvataria.show_menu()

# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.   

class admin(user):
    def __init__(self, name: str, password: str, location: str,*privileges:str):
        super().__init__(name, password, location)
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"\nAs an admin {self.name.title()} can:\n")
        for privilege in self.privileges:
            print(f"- {privilege.upper()}")
        print("\n")

god = admin("God","12345","heaven","Create life","Heal the injuried")

god.show_privileges()

# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

class privileges():
    def __init__(self,privileges:tuple):
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"\nAs an admin this user can:\n")
        for privilege in self.privileges:
            print(f"- {privilege.upper()}")
        print("\n")

class admin2(user):
    def __init__(self, name: str, password: str, location: str,*privilege:str):
        super().__init__(name, password, location)
        self.privileges = privileges(privilege)

user2 = admin2("William","1234","brazil","fly","run","modmenu")

user2.privileges.show_privileges()


