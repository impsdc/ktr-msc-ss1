class WeaponException(Exception):

    def __init__(self, weapon, name, RPGClass):
        if not weapon:
            self.message = f'{name} : I refuse to fight with my bare hands.'
        elif RPGClass == "Warrior" :
            self.message = f"{name} : I don 't need this stupid {weapon}! Don 't misjudge my powers !"
        elif RPGClass == 'Mage':
            self.message = f"{name} : {weapon}?? What should I do with this ?!"
        
        super().__init__(self.message)



