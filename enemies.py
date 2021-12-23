class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)
 
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)

class Dog(Enemy):
    def __init__(self):
        super().__init__(name="Dog", hp=20, damage=10)

class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf", hp=25, damage=15)


class Bear(Enemy):
    def __init__(self):
        super().__init__(name="Bear", hp=20, damage=15)


class Crocodile(Enemy):
    def __init__(self):
        super().__init__(name="Crocodile", hp=15, damage=20)

class Snake(Enemy):
    def __init__(self):
        super().__init__(name="Snake", hp=20, damage=20)


class BigPython(Enemy):
    def __init__(self):
        super().__init__(name="BigPython", hp=15, damage=20)


class Terrorist(Enemy):
    def __init__(self):
        super().__init__(name="Terrorist", hp=10, damage=10)

class Obadiah(Enemy):
    def __init__(self):
        super().__init__(name="Obadiah", hp=10, damage=10)

class Whiplash(Enemy):
    def __init__(self):
        super().__init__(name="Whiplash", hp=10, damage=10)

class Mandarin(Enemy):
    def __init__(self):
        super().__init__(name="Mandarin", hp=10, damage=10)

class JustinHammer(Enemy):
    def __init__(self):
        super().__init__(name="JustinHammer", hp=10, damage=10)


