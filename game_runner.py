from char import Character


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


game = Game()
if __name__ == '__main__':
    from weapon_list import create_common_weapon
    sword = create_common_weapon(game.player.level)
    print(game.player.name)
    game.player.inv.place_item(sword)
    # print(game.player.inv.inv)
    print(game.player.inv.weight)
