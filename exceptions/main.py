from Character import Character
from Warrior import Warrior
from Mage import Mage
from WeaponException import WeaponException

def main():
    bab = Warrior("bab")
    try :
        bab.tryToAttack("lol")
    except WeaponException as e:
        print(e)

    try:
        bab.tryToAttack("hammer")
    except WeaponException as e:
        print(e)

    bob = Mage("bob")
    try:
        bob.tryToAttack("wand")
    except WeaponException as e:
        print(e)

    try:
        bob.tryToAttack('')
    except WeaponException as e:
        print(e)

    bab.moveLeft()
    bob.life

    bab._unsheathe()


if __name__ == '__main__':
   main()