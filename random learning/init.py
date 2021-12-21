# A function inside a class is called a method

class User:
    """ This is a docstring. In order to call this help function type help(User). That call will
    display this text."""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.out = birthday

        name_split = full_name.split(" ")
        self.first_name = name_split[0]
        self.last_name = name_split[-1]
    
    def age(self):
        age = input("what is your age? ")
        self.age = age
        return age

user = User("David Bowman", 1979)
print(user.first_name, user.age())