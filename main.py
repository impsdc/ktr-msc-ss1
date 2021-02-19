from Character import Character
from Warrior import Warrior
from Mage import Mage

def main():
    perso = Character("paul", "class")
    print(perso.life)
    lol = perso.setName("lol")
    print(lol.name)

if __name__ == '__main__':
   main()