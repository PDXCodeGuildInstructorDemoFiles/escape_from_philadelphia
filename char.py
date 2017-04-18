from char_class import CharacterAttributes


class Character:
    def __init__(self, name):
        self.name = name
        self.cls = self.choose_class()

    def choose_class(self):
        print('Press 1 for Nuke Elf, 2 for Human, 3 for Zombie')
        d = {1: 'nuke_elf', 2: 'human', 3: 'zombie'}
        q = int(input('What class do you choose? '))
        return CharacterAttributes(d[q])

q = input('Hello what is your name? ')
player = Character(q)

print(player.name)
print(player.cls.name)

