# Code 1
class Enemy:

    def __init__(self,health,attack,movementspeed):
        self.health = health
        self.attack = attack
        self.movementspeed = movementspeed

enemy1 = Enemy("100","Ground",16)
enemy2 = Enemy("70","Air",10)

print ("Giant Stats")
print ("Health:", enemy1.health)
print ("Attack:", enemy1.attack)
print ("Movementspeed:", enemy1.movementspeed)

print ("Balloon Stats")
print ("Health:", enemy2.health)
print ("Attack:", enemy2.attack)
print ("Movementspeed:", enemy2.movementspeed)

# Code 2
class Myself:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

intro = Myself("Shivam",20,"Python")

print ("My name is", intro.name)
print (intro.age)
print (intro.course)

# Code 3
class Weapon:       # This creates a class named "Weapon". A class is like a blueprint or template for creating objects. Here, "Weapon" is the blueprint.
    def __init__(self,name,damage,ammo):        # "def" Means you're defining a function.
    # "__init__" is called the constructor. More specifically, it is Python's initializer method. Its job is to initialize an object.
    # "self" represents the current object being created. "DE" becomes "self". So "self" means the current object.

        self.name = name        # This creates an instance variable called "name". It stores "Desert Eagle" inside the object.
        self.damage = damage        # This creates an instance variable called "damage". It stores "200" inside the object.
        self.ammo = ammo        # This creates an instance variable called "ammo". It stores "7" inside the object.

DE = Weapon("Desert Eagle",200,7)       # This creates an object. Memory is allocated. Then Python automatically calls "__init__(DE,"Desert Eagle",200,7)". which fills the object. So now "DE" contains "Name = Desert Eagle", "Damage = 200", "Ammo = 7".

print ("Name:", DE.name)     # Python looks inside "DE". Finds "name = "Desert Eagle". Prints "Name: Desert Eagle".
print ("Damage:", DE.damage)     # Python looks inside object. Finds "damage = 200". Prints "Damage: 200".
print ("Ammo:", DE.ammo)     # Prints "Ammo = 7".
