from Character import Character
from Warrior import Warrior
from Mage import Mage

def main():
    jean = Warrior('Jean')
    paul = Mage('Paul')

    jean.attack('hammer')
    paul.attack('wand')


if __name__ == '__main__':
   main()