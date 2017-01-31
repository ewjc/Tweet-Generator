OOP Challange!

Problem 1: --------------------------------------------------------------
def sleep(name):
    print('{name} sleeps for 8 hours').format(name=name)

Problem 2:--------------------------------------------------------------
def eat(name, food):
    print('{name} eats {food}').format(name=name, food=food)
    if food == favoriteFood:
        print('YUM! {name} wants more {food}').format(name=name, food=food)

Problem 3:--------------------------------------------------------------
class Tiger(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Copy your eat function here and modify it to work as a method
    def eat(self, food):
        name = self.name
        self.food = food
        favoriteFood = 'meat'
        print('{name} eats {food}').format(name=name, food=food)
        if food == favoriteFood:
            print('YUM! {name} wants more {food}').format(name=name, food=food)
    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        name = self.name
        print('{name} sleeps for 8 hours').format(name=name)

Problem 4:--------------------------------------------------------------
class Bear(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        name = self.name
        self.food = food
        favoriteFood = 'fish'
        print('{name} eats {food}').format(name=name, food=food)
        if food == favoriteFood:
            print('YUM! {name} wants more {food}').format(name=name, food=food)

    def sleep(self):
        name = self.name
        print('{name} hibernates for 4 months').format(name=name)

Problem 5:--------------------------------------------------------------
class Animal(object):
    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood

    def eat(self, food):
        name = self.name
        favoriteFood = self.favoriteFood
        self.food = food
        print('{name} eats {food}').format(name=name, food=food)
        if food == favoriteFood:
            print('YUM! {name} wants more {food}').format(name=name, food=food)

    def sleep(self):
        name = self.name
        print('{name} sleeps for 8 hours').format(name=name)

# Implement the Tiger class here as a subclass of Animal
# Hint: Implement the initializer method only
class Tiger(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "meat")


# Implement the Bear class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Bear(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "fish")

    def sleep(self):
        name = self.name
        print('{name} hibernates for 4 months').format(name=name)
        
Problem 6:--------------------------------------------------------------
Problem 7:--------------------------------------------------------------
Problem 8:--------------------------------------------------------------
