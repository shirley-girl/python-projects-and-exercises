class GameCharacter:
    def __init__(self, name):
        self._name = name
        self.health = 100
        self.mana =50
        self._level = 1
    @property
    def name(self):
        return self._name 

    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self._health = 0
        elif new_health > 100:
            self._health = 100
        else:
            self._health = new_health

    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana

    
    @property
    def level (self):
        return self._level

    def level_up(self, increase):
        self._level += increase
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")
    
    
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"Mana: {self.mana}\n"
        )
gamer_1 = GameCharacter("Alpha Wolves")
print(gamer_1)

gamer_1.health -= 30
#gamer_1.level += 2 # this won't work since there's no level setter for updating level
gamer_1.mana -=10
gamer_1.health += 80
gamer_1.level_up(3)
print(gamer_1)