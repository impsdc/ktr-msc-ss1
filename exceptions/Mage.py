from Character import Character
from WeaponException import WeaponException

class Mage(Character):
    _RPGClass = 'Mage'
    _life = 70
    _agility= 3
    _strength= 10
    _wit = 10
    
    def __init__(self, name):
        self._name = name
        return print(f"{name} : May the gods be with me .")

    def tryToAttack(self, weapon):
        if weapon == "magic" or weapon == "wand":
            self.attack(weapon)
        else:           
            raise WeaponException(weapon, self.name, self.RPGClass)

    def attack(self, arg):
            print(f'{self.name} : Rrrrrrrrr ....')
            print(f"{self.name} : Feel the power of my {arg} !")
            return ""

    def moveRight(self):
        print(f"{self._name} : Moves right furtively.")

    def moveLeft(self):
        print(f"{self._name} : Moves left furtively.")

    def moveBack(self):
        print(f"{self._name} : Moves back furtively.")

    def moveForward(self):
        print(f"{self._name} : Moves forward furtively.")