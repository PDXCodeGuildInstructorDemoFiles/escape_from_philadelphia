from char_class import CharacterAttributes
from inventory import Inventory


class Character:
    def __init__(self, name):
        self.name = name
        self.cls = self.choose_class()
        self.inv = self.create_inv()
        self.level = 1

    def choose_class(self):
        print('Press 1 for Nuke Elf, 2 for Human, 3 for Zombie')
        d = {1: 'nuke_elf', 2: 'human', 3: 'zombie'}
        q = int(input('What class do you choose? '))
        return CharacterAttributes(d[q])

    def create_inv(self):
        return Inventory('player bag', 50)

if __name__ == '__main__':
    q = input('Hello what is your name? ')
    player = Character(q)

    print(player.name)
    print(player.cls.name)
