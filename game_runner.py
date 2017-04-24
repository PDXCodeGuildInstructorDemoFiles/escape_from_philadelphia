from char import Character
from loot_crate import LootCrate

class Game:
    def __init__(self):
        # self.map = Map()
        self.player = self.create_player()

    def create_monsters(self):
        pass

    def create_player(self):
        name = input("What is your name adventurer?: ")
        return Character(name)

    def start_game(self):
        pass

    def interface(self):
        while True:
            pass

    def console(self):
        print('story')
        player_alive = True
        while player_alive:
            q = input('What would you like to do? ')
            if 'attack' in q:
                pass
            elif 'look' in q and 'treasure' in q:
                crate = LootCrate(0, self.player.level)
                self.player.inv.place_item(crate.take_one_item())
            elif 'look' in q and 'bags' in q:
                self.player.inv.console(self.player)

if __name__ == '__main__':
    game = Game()
    game.console()
