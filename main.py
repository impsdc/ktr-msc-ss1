from Character import Character
from Warrior import Warrior
from Mage import Mage

def main():
   perso = Mage('bob')
   perso.moveForward()
   tqt = Character('cool', 'js')
   tqt.moveBack()


if __name__ == '__main__':
   main()