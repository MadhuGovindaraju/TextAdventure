import items, enemies, actions, world
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
 
        return moves


class StartingRoom1(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        ░░░░░░░██████████████████░░░░░░░
        ░░░░████▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓███░░░░░
        ░░░██▓▓█▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓█▓▓█░░░░
        ░░██████████▓▓▓▓▓▓▓▓██████████░░
        ░░██──────███████████───────██░░
        ░███───────██▓▓▓▓▓▓█────────███░
        ░████───────█▓▓▓▓▓▓█───────████░
        ░█▓██───────█▓▓▓▓▓▓█───────██▓█░
        ░██▓█───────█▓▓▓▓▓▓█───────█▓██░
        ████▓█──────█▓▓▓▓▓▓█──────█▓████
        █▓██▓█──────▀██████▀──────█▓██▓█
        █▓██▓█────────────────────█▓██▓█
        █▓████────────────────────████▓█
        █▓██▀──────────────────────▀██▓█
        █▓██──█▀▀▀▀▄▄──────▄▄▀▀▀▀█──██▓█
        ███───█─────▀██▄▄██▀─────█───███
        ░██───▀█▄▄▄▄█▀────▀█▄▄▄▄█▀───██░
        ░███────────────────────────███░
        ░░█▓█──────────────────────█▓█░░
        ░░█▓▓█────────────────────█▓▓█░░
        ░░█▓▓▓█──────────────────█▓▓▓█░░
        ░░█▓▓▓█──────────────────█▓▓▓█░░
        ░░█▓▓▓▓█▄──────────────▄█▓▓▓▓█░░
        ░░░█▓▓█▀█──▄▀▀▀▀▀▀▀▀▄──█▀█▓▓█░░░
        ░░░░█▓█─▀▄▄▀────────▀▄▄▀─█▓█░░░░
        ░░░░░█▓█─────▄▄▄▄▄▄─────█▓█░░░░░
        ░░░░░░█▓█▄▄▄██▓▓▓▓██▄▄▄█▓█░░░░░░
        ░░░░░░░█▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓█░░░░░░░
        ░░░░░░░░████████████████░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
             
                                     You are Ironman-1
             
        ***Tony stark is kidnapped by terrorist in Afghanistan and locked him in a cave to build a missiles for them.***
        ************Tony stark with the help of Dr Yensin builds the Iron man prototype and escapes the prison***
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass


class StartingRoom2(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        ████████████████████████████████████████████████████████████████
        █░░░░█░░░░░░░██░░░░░░░█░░████░░███░░░█████░░░█░░░░░░██░░████░░██
        █░░░░█░░██░░░██░░░██░░█░░░███░░███░░░░███░░░░█░░██░░██░░░███░░██
        ██░░██░░░░░░███░░░██░░█░░░░░█░░███░░█░░█░░█░░█░░░░░░██░░░░░█░░██
        ██░░██░░██░░░██░░░██░░█░░█░░█░░███░░██░░░██░░█░░██░░██░░██░░░░██
        █░░░░█░░███░░██░░░██░░█░░██░░░░███░░███████░░█░░██░░██░░███░░░██
        █░░░░█░░███░░██░░░░░░░█░░███░░░███░░███████░░█░░██░░██░░███░░░██
        ████████████████████████████████████████████████████████████████
        
                                   You are Ironman-2.
                              
        **** Obadiah Stane's scientists cannot duplicate Stark's miniaturized arc reactor, ***** 
            ** so Stane ambushes Stark at his home and steals the one from his chest. **
            **Stark manages to get to his original reactor to replace it before dying **
        
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

class StartingRoom3(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        ...................Ironman level-3..................
        ████████████████████████████████████████████████████████████████
        █░░░░█░░░░░░░██░░░░░░░█░░████░░███░░░█████░░░█░░░░░░██░░████░░██
        █░░░░█░░██░░░██░░░██░░█░░░███░░███░░░░███░░░░█░░██░░██░░░███░░██
        ██░░██░░░░░░███░░░██░░█░░░░░█░░███░░█░░█░░█░░█░░░░░░██░░░░░█░░██
        ██░░██░░██░░░██░░░██░░█░░█░░█░░███░░██░░░██░░█░░██░░██░░██░░░░██
        █░░░░█░░███░░██░░░██░░█░░██░░░░███░░███████░░█░░██░░██░░███░░░██
        █░░░░█░░███░░██░░░░░░░█░░███░░░███░░███████░░█░░██░░██░░███░░░██
        ███████████████████████████████████████████████████████████████
        
        You are in Morocco to try out the new stark industries F1 car.
        
               Whiplash and Mandarin planning to attack Tony stark.
               
        .............Suit up and shield from attack................
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} Power remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Fly(tile=self), actions.Attack(enemy=self.enemy), actions.Punch(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass


class Tonystarklab(MapTile):
    def intro_text(self):
        return """
        Hello sir, Good to hear back from home you.
        Pin : ***** 
        Door Opens. 
        Have a remarkable day sir!!!
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class JarvisAI(MapTile):
    def intro_text(self):
        return """
        Its another unremarkable decision sir.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

class HotelInMorocco(MapTile):
    def intro_text(self):
        return """
         ...... Tony stark is resting in Morocco hotel after fighting against whiplash...
         
          .... Mandarin enter the hotel lobby and paralyse the hotel staff with electro magnetic devices...
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

class HappyDrivesIn(MapTile):
    def intro_text(self):
        return """
          ..........Happy and Pepper Drives into F1 with ROLLS ROYCE.....
          ........Tony Boards the car and leaves the F1 circuit........
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

class Morocco(MapTile):
    def intro_text(self):
        return """
        
           Morocco, a North African country bordering the Atlantic Ocean and Mediterranean Sea..
                      
            Tony- stark arrives at Morocco in his private jet along with  Happy and Pepper.
            
                Tony is excited to try new F1 car on  Morocco F1 circuit.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class Morocco_Circuit(MapTile):
    def intro_text(self):
        return """

             Tony- stark arrives at Morocco F1 circuit and dressing for the race in pit stop room.

                Crowd chants - Tony , Tony Tony ...
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

class CallPepperHappy(MapTile):
    def intro_text(self):
        return """
        Tony- Jarvis call Pepper and Happy. Ask them to access the stark industries lab to stop Obadiah 
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

class ObadiahRoom(MapTile):
    def intro_text(self):
        return """
        A well suited up guy Obadiah is your fathers friend in meeting you with Crooked intentions.
        He has stolen the iron man suit arch reactor to power up his suit!!!
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

class StarkIndustires(MapTile):
    def intro_text(self):
        return """
        Enter Stark industries.
        Hello Sir, Good evening welcome to stark industries..
        Tony: Pepper take the central console room of the arch reactor. On 3 switch on master control....
        """

    def modify_player(self, player):
        # Room has no action on player
        pass
 
class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class Terrorist(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Terrorist())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Terrorist with AK47 with loaded rounds is firing at you!
             Dr.Yinsen is at risk please shield him.
             """
        else:
            return """
             Blown up Terrorist body found .
             """

class Obadiah(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Obadiah())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             Jarvis- Sir, Obadiah is attacking you with newly created suit.
             The suit is more power full than Mark-I version.
             Attack him
             """
        else:
            return """
             Unconscious Obadiah is laying on the floor.
             """

class Whiplash(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Whiplash())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             ....Whiplash enters the Monaco F1 circuit with electric ropes...
             ...Whiplash is cutting through fens and damaging the racing cars...
             """
        else:
            return """
             Disabled Whiplash is laying around and police is taking whiplash in to custody.
             """

class Mandarin(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Mandarin())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             Mandarin is a terrorist persona who uses his illegal genetic activities and Advanced Idea Mechanics
                           to manipulate the pepper and get hold of the iron man
             """
        else:
            return """
             Mandarin stuffed inside the ironman suit and blown up.
             """

class JustinHammer(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.JustinHammer())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             JustinHammer is a CEO of Hammer industries
             He want to build Hammer industries iron man suit. 
             He try to block Tony stark....  
             """
        else:
            return """
             Justin Hammer got punched from Tony stark.
             """

class F1Car(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.F1Car())

    def intro_text(self):
        return """
                            Tony all set with all racing equipment.
                    ....Tony stark stunned by sleek design want to drive car...
                    
                          ..........Tony boards the car......... 
        """

class StarkMissile(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.StarkMissile())

    def intro_text(self):
        return """
        There is a Missile box which is from Stark Industries.
        Pick it up along with Missile launcher. 
        StarkMissile is capable of destroying Terrorist under caves!!! 
        """

class BodyArmour(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.BodyArmour())

    def intro_text(self):
        return """
        Tony built the BodyArmour in caves.
        It's a prototype of Iron mark-I. It destroy the enemy and fly to close by range.
        """

class Jarvis(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.BodyArmour())

    def intro_text(self):
        return """
        Jarvis- Good morning sir.
        Welcome back. What you like to do today sir.
        Tony- Jarvis create secured directory move data from stark industries server my directory.
        Name the project IRON MAN MARK -1 to record all data and statics 
        """

class FireBlaze(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.FireBlaze())

    def intro_text(self):
        return """
        Uses high intensity fire to burn the opponents.
        """

class IronManSuit(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.FlyingIronManSuit())

    def intro_text(self):
        return """
        Tony enter his lab and find the old arch reactor....
        Iron man Mark-I powered the old reactor...
        Tony flys to locate Obadiah....
        """

class FlyingIronManSuit(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.FlyingIronManSuit())

    def intro_text(self):
        return """
        FlyingIronManSuit can reach Tony stark in remote of remote locations to shield from enemy attack.
        It's a  Iron mark-II suit with Jarvis AI system.
        """
class FlyingIronManGloves(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.FlyingIronManGloves())

    def intro_text(self):
        return """
        FlyingIronManGloves can reach Tonystark in remote and narrow locations to attack enemy.
        """

class CaveRoom(MapTile):
    def intro_text(self):
        return """
            You are locked in a cave room for preparing the missile for terrorist ...
            ... you have Dr.Yensin who treated your wound!
            """
    def modify_player(self, player):
        #Room has no action on player
        pass

class CaveRoom2(MapTile):
    def intro_text(self):
        return """
            Cave room two is heavily guarded by terrorist with AK47...
            ... it has thick iron door...
            """
    def modify_player(self, player):
        #Room has no action on player
        pass

class CaveRoom3(MapTile):
    def intro_text(self):
        return """
            Cave room 2 is heavily guarded by terrorist with AK47...
            ... it has thick iron door...
            """

    def modify_player(self, player):
        #Room has no action on player
        pass

class FlyoffromCave(MapTile):
    def intro_text(self):
        return """
            Pull trigger and enable flight mode ...
            ... you will be landing into safe place where Col.Rodes will come and pick you!


            Victory is yours!
            """


    def modify_player(self, player):
        player.victory = True


class FlyRooftop(MapTile):
    def intro_text(self):
        return """
            Tony- Pepper on 3 switch on the master controller ...
            ... Arch reactor blows of the roof top... Obadiah suit blown.
            
            Tony- Fly off the roof top. 
            
            Jarvis- Have good rest of the day sir. Nice Weather you can enjoy a ice cream.  

            """

    def modify_player(self, player):
        player.victory = True


class BlowMandarin(MapTile):
    def intro_text(self):
        return """
            Tony- Jarvis prepare the suit mark-III with blast configuration ...
            
            ... Jarvis - Sir its very dangers configuration and we need to do terabytes calculation.
            
            Tony - Jarvis some time we need to run before walking, do it as per instruction ..

                Suit mark-III with blast configuration suited up to Mandarin and suit is blown up.

            """

    def modify_player(self, player):
        player.victory = True