from Character import Character

class Warrior(Character):
    _RPGClass = 'Warrior'
    _life = 100
    _agility= 10
    _strength= 8
    _wit = 3
    
    def __init__(self, name):
        self._name = name
        return print(f"{name} : My name will go down in history !")
        

    def attack(self, arg):
        if arg == 'hammer' or arg == "sword":
            print(f'{self.name} : Rrrrrrrrr ....')
            print(f"{self.name} : I'll crush you with my {arg} !")
            return ''
        else:
            print(f'{self.name} does not attack')
            return ''