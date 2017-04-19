from char_class import CharacterAttributes
from inventory import Inventory


class Character:
    def __init__(self, name):
        self.name = name
        self.cls = self.choose_class()
        self.inv = self.create_inv()
        self.level = 1

    def choose_class(self):
        print('''Press 1 for Nuke Elf, 2 for Human, 3 for Zombie, 4 for Lemur, 5 for Gorilla, 6 for Cyborg, '
              7 for Technovore, 8 for Mid-night Elf or 9 for Bear''')
        d = {1: 'nuke_elf', 2: 'human', 3: 'Charasaurus Rex: First Bite', 4: ''}
        q = int(input('What class do you choose? '))
        return CharacterAttributes(d[q])

    def create_inv(self):
        return Inventory('player bag', 50)

if __name__ == '__main__':
    q = input('Hello what is your name? ')
    player = Character(q)

    print(player.name)
    print(player.cls.name)
