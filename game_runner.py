from map import Map


class Game:
    def __init__(self):
        self.map = Map()

    def create_monsters(self):
        pass

    def create_player(self):
        pass
        name = input("What is your name adventurer?: ")

    def start_game(self):
        pass

    def interface(self):
        while True:
            command = input("Type Command: ( n s e w a(t)tack cast heal x:exit )\n>>> ")

            if command[:2] == 'at' or 't' == command[:1] or command[:1] == 'w' or ' ' == command[:1] or '' == command[
                                                                                                              :1]:
                if check_proximity():
                    player_attack(command[command.find(" ") + 1:])
                else:
                    move(0)

            elif command[:4] == 'cast' or 'c' == command[:1]:
                cast_spell(command[command.find(' ') + 1:])
                screen.head[0] = 1
                screen.mapit()

            elif command[:4] == 'heal' or 'h' == command[:1]:

                # if len(command) > 4:
                if command.find(' ') > -1:
                    heal_self(command[command.find(' '):])
                else:
                    heal_self()
                screen.head[0] = 0
                screen.mapit()

            else:
                for i in range(len(command)):
                    if command[i] == 'x':
                        if input('      Are you sure you want to quit? (c) ') == 'c':
                            quit()
                    elif command[i] == 'n' or '2' == command[i] or 'A' == command[i]:
                        move(2)
                    elif command[i] == 's' or '8' == command[i] or 'B' == command[i]:
                        move(8)
                    elif command[i] == 'e' or '6' == command[i] or 'C' == command[i]:
                        move(6)
                    elif command[i] == 'q' or '4' == command[i] or 'D' == command[i]:
                        move(4)
                    elif command[i] == '1':
                        move(1)
                    elif command[i] == '3':
                        move(3)
                    elif command[i] == '7' or 'a' == command[i]:
                        move(7)
                    elif command[i] == '9' or 'd' == command[i]:
                        move(9)


game = Game()