class Character:
    
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

player = Character("Soldier", 100, "Desert Eagle")
enemy = Character("Devil", 1000, "Katana")

print ("Player: ", player.name)
print ("Health: ", player.health) 
print ("Weapon: ", player.weapon)

print ("Player: ", enemy.name)
print ("Health: ", enemy.health) 
print ("Weapon: ", enemy.weapon)


class Player:
    def __init__(self,mana):
        self.mana = mana  # Instance Variable

player1 = Player(100)
print ("Mana: ", player1.mana)


class Player:

    game_name = "Battle Arena"  # Class Variable (game_name) 

    @classmethod
    def show_game(cls):

        print(cls.game_name)  # Current class

Player.show_game()


class Weapon:

    def __init__ (self, name, damage):
        self.name = name
        self.damage = damage

a = Weapon("AK47", 70)

print (a.name, a.damage)



# Encapsulation
class Golem:
    def __init__(self):
        self.__health = 1000

    def take_damage (self,damage):
        self.__health -= damage

    def show_health(self):
        print (self.__health)

Troop = Golem()

Troop.take_damage(645)
Troop.show_health()


# Inheritance.
class Dragon:
    def move (self):
        print ("Troops are Moving")

class Giant(Dragon):
    def walk (self):
        print ("Giants are Walking")

a = Giant()
a.move()
a.walk()


# Polymorphism
class Warrior:

    def attack(self):
        print("Sword Attack")


class Archer:

    def attack(self):
        print("Arrow Attack")


players = Warrior(), Archer()

for player in players:
    player.attack()