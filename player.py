﻿import random 
import items, world
 
class Player():
    def __init__(self):
        #self.inventory = [items.Gold(15), items.Pillow(), items.Rock()] #Inventory on startup
        self.inventory = [items.StarkMissile(), items.BodyArmour(),items.FlyingIronManSuit()]  # Inventory on startup
        self.hp = 100 # Health Points
        self.location_x, self.location_y = world.starting_position  #(0, 0)
        self.victory = False #no victory on start up
        self.levell = 1

    def fly(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0   #Greater than zero value then you are still alive
 
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        self.move(dx=0, dy=1)
 
    def move_east(self):
        self.move(dx=1, dy=0)
 
    def move_west(self):
        self.move(dx=-1, dy=0)

    def punch(self, enemy):
        print("You punched the {}!\n".format(enemy.name))
        print("Suit Current Power is {}.\n".format(self.hp))
        self.hp += enemy.hp
        print("You got Bounty for punching {} and Suit power is increased by {}.".format(enemy.name, self.hp))

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
     action_method = getattr(self, action.method.__name__)
     if action_method:
                action_method(**kwargs)