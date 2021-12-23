# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self,  name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# Gold class will be a child or subclass of the superclass Item
class Pelladium(Item):
    # __init__ is the contructor method
    def __init__(self, amt): 
        self.amt = amt # attribute of the Gold class
        super().__init__(name="Pelladium",
                         description="Pelladium {} is the core of the Archreactor which powers Ironman Suit.".format(str(self.amt)),
                         value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
class StarkMissile(Weapon):
    def __init__(self):
        super().__init__(name="StarkMissile",
                         description="StarkMissile can kill the Target enemy from far.",
                         value=15,
                         damage=15)

class BodyArmour(Weapon):
    def __init__(self):
        super().__init__(name="BodyArmour",
                         description="BodyArmour can shield from any kind of enemy attack and shield the TonyStark in cave.",
                         value=15,
                         damage=15)

class FlyingIronManSuit(Weapon):
    def __init__(self):
        super().__init__(name="FlyingIronManSuit",
                         description="FlyingIronManSuit can reach Tonystark in remote of remote locations to shield from enemy attcak.",
                         value=15,
                         damage=15)

class FlyingIronManGloves(Weapon):
    def __init__(self):
        super().__init__(name="FlyingIronManGloves",
                         description="FlyingIronManGloves can reach Tonystark in remote and narrow locations to attack enemy.",
                         value=15,
                         damage=15)

class FireBlaze(Weapon):
    def __init__(self):
        super().__init__(name="FireBlaze",
                         description="Open FireBlaze on terrorist and destroy all stark industries missiles.",
                         value=10,
                         damage=15)

class F1Car(Weapon):
    def __init__(self):
        super().__init__(name="F1Car",
                         description="F1Car is the super car in Morocco Circuit.",
                         value=10,
                         damage=15)