
from unicodedata import name


class Enemy(object):

    def __init__(self, name, hitpoints=0) -> None:
        self.name = name
        self.hitpoints = hitpoints
    
    def take_damage(self, damage):
        if damage <= self.hitpoints:
            self.hitpoints-=damage
            print(f"{self.name} took damage of {damage}.Hitpoints remaining {self.hitpoints}")
        if self.hitpoints<=0:
            print(f"{self.name} lost")


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hitpoints=25)

    def dodge(self):
        import random
        return random.randint(0,3)

    def take_damage(self, damage):
        ran = self.dodge()
        if ran == 3:
            self.hitpoints-=0
            print(f"{self.name} dodged")
        else:
            if damage <= self.hitpoints:
                self.hitpoints-=damage
                print(f"{self.name} took damage of {damage}.Hitpoints remaining {self.hitpoints}")
        if self.hitpoints<=0:
            print(f"{self.name} lost")


class dragon(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hitpoints=25)
        self.lives = 2
    
    def take_damage(self, damage):
        if self.lives>0:
            if damage <= self.hitpoints:
                    self.hitpoints-=damage
                    print(f"{self.name} took damage of {damage}.Hitpoints remaining {self.hitpoints}")
        if self.hitpoints<=0:
            if self.lives>0:
                print(f"{self.name} lost 1 life. {self.lives-1} remaining")
                self.lives-=1
                self.hitpoints = 25
            else:
                print("{self.name} lost")

        



drag = Enemy("drag", 150)
drag.take_damage(50)
drag.take_damage(100)
troll = Troll("troll")
troll.take_damage(20)
troll.take_damage(5)

tom = dragon("tom")
tom.take_damage(25)
tom.take_damage(20)
tom.take_damage(5)



        