class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 100
       # self.health = health
       # Omitted health parameter from class definition
       # Parent and child parameters need to match
    
    def walk(self):
        self.health = self.health - 1
        return self
    
    def run(self):
        self.health = self.health - 5
        return self
        
    def displayHealth(self):
        print("Health", self.health)
        return self
        
#animal1 = Animal("Donkey", 100)
#animal1.walk()
#animal1.walk()
#animal1.walk()
#animal1.run()
#animal1.run()
#animal1.displayHealth()

class Dog(Animal): 
    
    def __init__(self,name): 
        super(Dog,self).__init__(name)
        self.name = name
        self.health = 150
        
    def pet(self):
        self.health = self.health + 5
        return self

dog1 = Dog("Tommy")
dog1.walk()
dog1.walk()
dog1.walk()
dog1.run()
dog1.run()
dog1.pet()
dog1.displayHealth()

class Dragon(Animal):
    
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.name = name
        self.health = 170
        
    def fly(self):
        self.health = self.health - 10
        return self

    def displayHealth(self):
        super(Dragon,self).displayHealth()
        print("I am a dragon")
        
dragon1 = Dragon("Dragon-name")

dragon1.displayHealth()
