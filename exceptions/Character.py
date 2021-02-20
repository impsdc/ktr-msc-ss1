from Movable import Movable
from WeaponException import WeaponException
class Character(Movable, WeaponException):
    _life = 50
    _agility= 2
    _strength= 2
    _wit= 2

    def __init__(self, name, RPGCLass):
        self._name = name
        self._RPGClass = RPGCLass

    @property
    def name(self):
        return self._name

    @property
    def RPGClass(self):
        return self._RPGClass

    @property
    def life(self):
        return self._life

    @property
    def agility(self):
        return self._agility

    @property
    def strength(self):
        return self._strength
    
    @property
    def wit(self):
        return self._wit

    def attack(self, arg):
        print(f'{self.name} : Rrrrrrrrr ....')

    # Do not overide this method !
    def _unsheathe(self):
        print(f"{self.name} : unsheathes his weapon.")
