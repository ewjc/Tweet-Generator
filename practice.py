class Tiger:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{self} ate some {food}').format(self=self, food=food)
        
