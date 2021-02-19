from Character import Character
from Warrior import Warrior
from Mage import Mage


def main():
   bob = Character('bob', 'class')
   bob.moveForward()
   bib = Mage("bib")
   bib.moveBack()
   bab = Warrior("bab")
   bab.moveLeft()


if __name__ == '__main__':
   main()