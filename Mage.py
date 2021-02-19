from Character import Character

class Mage(Character):
    _RPGClass = 'Mage'
    _life = 70
    _agility= 3
    _strength= 10
    _wit = 10
    
    def __init__(self, name):
        self._name = name
        return print(f"{name} : May the gods be with me .")

    def attack(self, arg):
        if arg == 'magic' or arg == "wand":
            print(f'{self.name} : Rrrrrrrrr ....')
            print(f"{self.name} : Feel the power of my {arg} !")
            return ""
        else:
            print(f'{self.name} does not attack')
            return ''

    def moveRight(self):
        print(f"{self._name} : Moves right furtively.")

    def moveLeft(self):
        print(f"{self._name} : Moves left furtively.")

    def moveBack(self):
        print(f"{self._name} : Moves back furtively.")

    def moveForward(self):
        print(f"{self._name} : Moves forward furtively.")