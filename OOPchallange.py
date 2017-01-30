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
Problem 6:--------------------------------------------------------------
Problem 7:--------------------------------------------------------------
Problem 8:--------------------------------------------------------------
