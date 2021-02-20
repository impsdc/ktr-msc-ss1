from Character import Character
from WeaponException import WeaponException

class Warrior(Character):
    _RPGClass = 'Warrior'
    _life = 100
    _agility= 10
    _strength= 8
    _wit = 3
    
    def __init__(self, name):
        self._name = name
        return print(f"{name} : My name will go down in history !")
        
    def tryToAttack(self, weapon):
        if weapon == "hammer" or weapon == "sword":
            self.attack(weapon)
        else:           
            raise WeaponException(weapon, self.name, self.RPGClass)

    def attack(self, arg):
            print(f'{self.name} : Rrrrrrrrr ....')
            print(f"{self.name} : I'll crush you with my {arg} !")
            return ''
        
    def moveRight(self):
        print(f"{self._name} : Moves right like a bad boy.")

    def moveLeft(self):
        print(f"{self._name} : Moves left like a bad boy.")

    def moveBack(self):
        print(f"{self._name} : Moves back like a bad boy.")

    def moveForward(self):
        print(f"{self._name} : Moves forward like a bad boy.")