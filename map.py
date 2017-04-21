from random import choice
# import Map_renderer from map_renderer

#######################################################

# RECEIVE DIRECTIVES FOR MOVEMENT
# GENERATE MAP
# INHIBIT UNLAWFUL MOVES
# GENERATE WALLS

class Map:
    '''
    METHODS:
        move(num)
        123
        406
        789
    '''

    def __init__(self, player, monsters, ma_fn_ref, lvl_fn_ref, get_lives_fn, get_mon_fn):
        '''INITIALIZE VARIALBES'''
        self.player = player
        self.monsters = monsters

        self.monster_attack = ma_fn_ref
        self.level_fn = lvl_fn_ref
        self.get_lives = get_lives_fn
        self.get_monsters = get_mon_fn

        self.MAP_SIZE = 24
        self.map_row = " . . . . . . . . . . . . . . . . . . . . . . . ."
        self.map_rows = self.initialize_map(4)  # []
        self.frame_i = [0]
        self.head = [0]
        self.message_key = ['', '', '']
        self.this_monster = [0]
        self.monster_modes = ['ROAM', 'FIGHT']



        '''
        EXPAND MAPS
        012
        345
        678
        '''
        self.maps = [[[],[],[]],[[],[],[]],[[],[],[]]]
        self.maps[0][1] = self.initialize_map(1)
        self.maps[1][1] = self.map_rows
        self.maps[2][1] = self.initialize_map(7)

        self.maps[0][0] = self.initialize_map(0)
        self.maps[1][0] = self.initialize_map(3)
        self.maps[2][0] = self.initialize_map(6)

        self.maps[0][2] = self.initialize_map(2)
        self.maps[1][2] = self.initialize_map(5)
        self.maps[2][2] = self.initialize_map(8)

        self.current_map = [1,1]

        print( self.maps[self.current_map[0]][self.current_map[1]] )

    def initialize_map(self, x):
        '''INITIALIZE MAP'''

        if x == 0:
            mp = []
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")

        if x == 3:
            mp = []
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # . # # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # # # . # # .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . . . ; * ; ; .")
            mp.append(" # . . . . . . # . . . . . . . . . # . ; * ; ; .")
            mp.append(" # . . . . . . . . . . . * * . . . # . ; * ; ; .")
            mp.append(" # . . . . . . # . . . . * * . . . # . * * * * .")
            mp.append(" # . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # # # . # # # # . . . . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # # # # # # # # . # # . * * * * .")
            mp.append(" # . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . . . . . . . . . . . . . . . .")

        elif x == 6:
            mp = []
            mp.append(" # . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # . # # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # # # . # # .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . ; * ; ; .")
            mp.append(" # . . . . . . # . . . . . . . . . # . ; * ; ; .")
            mp.append(" # . . . . . . . . . . . X X . . . # . ; * ; ; .")
            mp.append(" # . . . . . . # . . . . X X . . . # . * * * * .")
            mp.append(" # . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # . . . . . . . . . ; . * * * * .")
            mp.append(" # # # . # # # # . . . . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # # # # # # # # # # # . * * * * .")
            mp.append(" # . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")

        if x == 1:
            mp = []
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . # # # # # # # # # # # # # # # # # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . # . . . . .")
            mp.append(" . . . . . . . . . . . # . # . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # . X . # . . . . . .")
            mp.append(" . . . . . . . . . . . . # . . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # # # # # . . . . . .")
            mp.append(" . . . . . . . . . . . # . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # . # # # # # # # # # # # .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")

        if x == 4:
            mp = []
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . # . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # # # # # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . # # # # # . # # # # # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # # # # # # # # # . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")

        elif x == 7:
            mp = []
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . # # # # # # . # # # # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # # # # # # .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . ; * ; ; .")
            mp.append(" . . . . . . . # . . . . . . . . . # . ; * ; ; .")
            mp.append(" . . . . . . . . . . . . . . . . . # . ; * ; ; .")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # # # # # # # # . . . . . . . . . # . * * * * .")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" . . . . . . . # # # # # . # # # # # . * * * * .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")


        if x == 2:
            mp = []
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . # # # # # # # # # # # # # # # # # . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . # . . . . #")
            mp.append(" . . . . . . . . . . . # . # . . . # . . . . . #")
            mp.append(" . . . . . . . . . . . . . # . X . # . . . . . #")
            mp.append(" . . . . . . . . . . . . # . . . . # . . . . . #")
            mp.append(" . . . . . . . . . . . . . # # # # # . . . . . #")
            mp.append(" . . . . . . . . . . . # . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" # # # # # # # # # # # . # # # # # # # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")

        if x == 5:
            mp = []
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . # . . . # . . . . . #")
            mp.append(" . . . . . . . . . . . . . # . X . # . . . . . #")
            mp.append(" . . . . . . . . . . . . . # . X . # . . . . . #")
            mp.append(" . . . . . . . . . . . . . # # # # # . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . # # # # # . # # # # # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # # # # # # # # # . # . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")

        elif x == 8:
            mp = []
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . # # # # # # . # # # # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # # # # # # #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . ; * ; ; #")
            mp.append(" . . . . . . . # . . . . . . . . . # . ; * ; ; #")
            mp.append(" . . . . . . . . . . . . . . . . . # . ; * ; ; #")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * #")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * #")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * #")
            mp.append(" # # # # # # # # . . . . . . . . . # . X X X X #")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * #")
            mp.append(" . . . . . . . # # # # # . # # # # # . * * * * #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")

        return mp

        # maprws = []
        # for r in range(self.MAP_SIZE):
        #     maprws.append(self.map_row)
        # return maprws



    def reincarnate(self, player, monsters):
        """FOR WHEN PLAYER DIES BUT HAS MORE LIVES"""

        print("Killed by level {} {}.    Don't forget to heal!".format(self.level_fn(), monsters[self.this_monster[0]].type))
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################ !!!!YOU DIED!!!! ################ ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("#############  WOULD YOU LIKE TO BE  ############# ")
        print("#############    REINCARNATED? (n)   ############# ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        print("################################################## ")
        self.hud(player)
        verdict = input('Reincarnate? ( any key or (n)o ) : ')
        if verdict.lower() == 'n':
            quit()
        player.health = 100
        player.position[0] = 12
        player.position[1] = 12
        self.head[0] = 5
        self.mapit(player, monsters)
        #


    def monster_go(self, player, monsters):
        '''MONSTERS TURN DETERMINATION'''

        # fizz = lambda v: v

        self.message_key[1] = ''
        self.message_key[2] = ''
        for m in range(len(monsters)):
            arg = 2
            if abs(monsters[m].position[0] - player.position[0]) < arg and arg > abs(
                            monsters[m].position[1] - self.get_index_from_bit(player.position[1])):
                monsters[m].mode = self.monster_modes[1]
            else:
                monsters[m].mode = self.monster_modes[0]

            if monsters[m].mode == 'ROAM':
                self.head[0] = 0
                self.monster_move(monsters, m)
            elif monsters[m].mode == 'FIGHT':
                self.message_key[1] = 'm1'
                self.head[0] = 2
                self.this_monster[0] = m
                self.monster_attack(m)

    def unobstructed(self, arg):
        '''CHECK FOR OBSTRUCTION TO MOVEMENT'''
        print(arg)
        if arg == " #":
            return False
        else:
            return True

    def monster_move(self, monsters, mm=0):


        '''maps the monster to a new position on map'''

        m = mm
        # for m in range(2):
        mon_row = monsters[m].position[0]
        mon_col = monsters[m].position[1]
        # mon_ind = MAP_SIZE - mon_row

        rand_verticle = choice([-1, 0, 1])
        rand_horizontal = choice([-1, 0, 1])

        proposed0 = 0
        proposed1 = 0

        mon_colm = mon_col
        if monsters[m].position[0] < 1:
            monsters[m].position[0] = 1
        elif monsters[m].position[0] > 22:
            monsters[m].position[0] = 22


        else:
            # monsters[m].position[0] += choice([-1, 0, 1])
            proposed0 = monsters[m].position[0] + rand_horizontal
        #
        if monsters[m].position[1] < 2:
            monsters[m].position[1] = 2
        elif monsters[m].position[1] > 22:
            monsters[m].position[1] = 22


        else:
            # monsters[m].position[1] += choice([-1, 0, 1])
            proposed1 = monsters[m].position[1] + rand_verticle
        #

        try:
            print('[proposed0][(proposed1  : {} , {} '.format(proposed0, proposed1 ) )
            proposed_terr = self.maps[self.current_map[0]][self.current_map[1]][proposed0][(proposed1 - 1) * 2: ((proposed1 - 1) * 2) + 2]
            print("proposed_terr : '{}' ".format( proposed_terr) )
        except IndexError:
            proposed_terr = " ."

        # if " #" != proposed_terr:
        if self.unobstructed(proposed_terr):
            # print("proposed_terr : ' #' is not '{}' ".format(proposed_terr))
            monsters[m].position[0] += rand_horizontal
            monsters[m].position[1] += rand_verticle


        # try:
        newrow = self.maps[self.current_map[0]][self.current_map[1]][mon_row][: (mon_colm - 1) * 2]
        # except IndexError:
        #     pass
        #
        ##### THIS IS THE TEST: ######################
        # terr = self.maps[self.current_map[0]][self.current_map[1]][mon_row][(monsters[m].position[1] - 1) * 2: ((monsters[m].position[1] - 1) * 2) + 2]


        # try:
        terr = self.maps[self.current_map[0]][self.current_map[1]][monsters[m].position[0]][(monsters[m].position[1] - 1) * 2: ((monsters[m].position[1] - 1) * 2) + 2]
        # except IndexError:
        #     pass


        ##############################################

        # terr_prog = ".,•º∞*"
        terr_prog = monsters[0].biom
        # print('terr : "{}" '.format(terr))
        newrow += " " + terr_prog[(terr_prog.find(terr[1]) + 1) % len(terr_prog)]
        newrow += self.maps[self.current_map[0]][self.current_map[1]][mon_row][(mon_colm) * 2:]
        self.maps[self.current_map[0]][self.current_map[1]][mon_row] = newrow

    def check_proximity(self, monsters, player, arg=2):
        '''returns True if target is within proximity of arg. 
        2 == adjacent square; 
        3 == 2 spaces away
        1 == same square
        '''

        for m in range(len(monsters)):
            if abs(monsters[m].position[0] - player.position[0]) < arg and arg > abs(
                            monsters[m].position[1] - self.get_index_from_bit(player.position[1])):
                self.this_monster[0] = m
                return True
        return False

    def message(self, x, additional='', monsters=[]):
        '''MESSAGE SYSTEM : TO BE REVAMPED FOR NEW GAME'''
        return {
                   'cast': 'Magic spell cast, doing some damage.',
                   'h': 'You have been healed',
                   'g90': 'Gained 90 Gold.',
                   'g50': 'Gained 50 Gold.',
                   'g19': 'Gained 19 Gold.',
                   'g9': 'Gained 9 Gold.',
                   'g11': 'Gained 11 Gold.',
                   'g20': 'Gained 20 Gold.',
                   'g7': 'Gained 7 Gold.',
                   'g5': 'Gained 5 Gold.',
                   'g1': 'Gained 1 Gold.',

                   'm1': 'Fight monster: {} with {}({}) HP:{} '
                       .format(self.get_monsters()[self.this_monster[0]].type, self.get_monsters()[self.this_monster[0]].inventory[0]['name'],
                               self.get_monsters()[self.this_monster[0]].inventory[0]['damage'], self.get_monsters()[self.this_monster[0]].health),

                   '.': 'Nothing to say.',
                   '': '',

                   # THIS IS NOT WORKING:
                   'killedit': 'You have slain the monster!',

                   'looted': 'You have looted the corpse',
                   'dmg': '- DAMAGE = '
               }[x] + additional


    def hud(self, player):
        '''HEADS UP DISPLAY : TEN LINES X48 CHARACTERS
        
        '''
        # print("################################################# ")
        #
        # print("# ")
        # print("# ")
        # print("# ")
        # print("# ")
        # print("# ")
        # print("# ")
        # print("# ")
        # print("# ")
        # print("# ")
        # print("# ")
        # print("# {}".format())
        # print("# {}".format())
        # print("# {}".format())
        # print("# {}".format())
        # print("# {}".format())
        # print("# {}".format())
        # print("# {}".format())
        # print("# {}".format())
        # print("# {}".format())
        # print("# {}".format())

        print("################################################# ")

        print("LEFT : {} {}  HEALTH: {}  {}".format(player.inventory[0]['name'], player.inventory[0]['damage'],
                                                    player.health,
                                                    self.message(self.message_key[2][:3],
                                                                 self.message_key[2][self.message_key[2].find(' '):])))
        print("RIGHT: {}({})    GOLD  : {} ".format(player.inventory[1]['name'], player.inventory[1]['block'],  player.gold))
        # print(":POTION ^(f)                  (r)^ STAFF:")
        print(self.message(self.message_key[1]), self.message(self.message_key[0]))

        # HELPER FUNCTION FOR mapit()

    def get_index_from_bit(self, c):
        '''HELPER FUNCTION : TRANSLATES BINARY NUMBER TO INDEX'''
        # for i in range(self.MAP_SIZE):
        #     if c == 1 << i:
        #         return self.MAP_SIZE - i
        return c

    def header(self, player={}):
        '''PRINTS HEADER'''
        # print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        self.frame_i[0] += 1
        print('Frame # {}  Level # {}   Lives : {} '.format(self.frame_i[0], self.level_fn() , self.get_lives() ))

        if self.head[0] == 0:
            print("######################################## Move Key: 123 | 123")
            print("################ A D V E N T U R E ##### n s e w # q*e | 4*6")
            print("################################################## asd | 789")
            print("##################### MAP{}:{} ##################### ".format(self.current_map[0], self.current_map[1]))

        elif self.head[0] == 1:
            print("################################################## ")
            print("################# A SPELL IS CAST ################ ")
            print("################################################## ")
        elif self.head[0] == 2:
            print("################################################## ")
            print("################ MONSTER ATTACKED ################ ")
            print("################################################## ")
        elif self.head[0] == 3:

            print("Killed by level {} {}.  Don't forget to heal!".format(self.level_fn(), self.get_monsters()[0].type))
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################ !!!!YOU DIED!!!! ################ ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            self.hud(player)

        elif self.head[0] == 4:
            print("################################################## ")
            print("############### !!!! YOU WON !!!! ################ ")
            print("################################################## ")
        elif self.head[0] == 5:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
            print("######## !! YOU HAVE BEEN REINCARNATED !! ######## ")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")

    def mapit(self, player, monsters, a='', b=''):
        '''PRINTS MAP : CALLED INTERNALLY'''
        col = player.position[1]
        row = player.position[0]
        self.header()
        ind = self.MAP_SIZE - row

        ### MONSTER
        for m in range(len(monsters)):
            mon_row = monsters[m].position[0]
            mon_col = monsters[m].position[1]
            mon_colm = mon_col
            newrow = self.maps[self.current_map[0]][self.current_map[1]][mon_row][: (mon_colm - 1) * 2]
            newrow += monsters[m].avatar
            newrow += self.maps[self.current_map[0]][self.current_map[1]][mon_row][(mon_colm) * 2:]
            self.maps[self.current_map[0]][self.current_map[1]][mon_row] = newrow

        for r in range(row):
            print(self.maps[self.current_map[0]][self.current_map[1]][r], r)
        colm = self.get_index_from_bit(col)
        newrow = self.maps[self.current_map[0]][self.current_map[1]][row][: (colm - 1) * 2]
        thisrow = self.maps[self.current_map[0]][self.current_map[1]][row][(colm - 1) * 2:(colm) * 2]
        if thisrow == ' .':
            player.gold += 1
            self.message_key[0] = 'g1'
        elif thisrow == ' •':
            player.gold += 7
            self.message_key[0] = 'g7'
        elif thisrow == ' :':
            player.gold += 19
            self.message_key[0] = 'g19'
        elif thisrow == ' ;':
            player.gold += 90
            self.message_key[0] = 'g90'
            # ".,•º∞*"
        elif thisrow == ' ∞':
            player.gold += 50
            self.message_key[0] = 'g50'
        elif thisrow == ' º':
            player.health += 33
            self.message_key[0] = 'h'
        elif thisrow == ' *':
            player.health += 26
            self.message_key[0] = 'h'
        elif thisrow == ' ,':
            player.gold += 5
            self.message_key[0] = 'g5'
        elif thisrow == ' x':
            player.re_equip()
            self.message_key[0] = 'looted'
        elif thisrow == ' X':
            player.re_equip()
            player.gold += 5000
            self.message_key[0] = 'looted'
        else:
            self.message_key[0] = ''
        ### HERO
        newrow += "  "  # trail
        newrow += self.maps[self.current_map[0]][self.current_map[1]][row][(colm) * 2:]
        self.maps[self.current_map[0]][self.current_map[1]][row] = newrow
        p = self.maps[self.current_map[0]][self.current_map[1]][row][: (colm - 1) * 2]
        p += player.avatar
        p += self.maps[self.current_map[0]][self.current_map[1]][row][(colm) * 2:]
        print(p, row)
        for x in range(1, ind):
            print(self.maps[self.current_map[0]][self.current_map[1]][row + x], row + x)
        self.hud(player)



        # CALCULATE TRANSLATION OF position
    def move(self, arg, player, monsters):
        ''' RECEIVE INPUT : CALLED EXTERNALLY
        map.move(number)
        123
        406
        789
        RETURNS RESULTING EVENT:
        SUCCESS, FAIL=HIT WALL
        '''
        # INSERT CONDITIONALS FOR WALL ENCOUNTERS
        print("move arg: ", arg)
        temp_y0 = player.position[0]
        temp_x1 = self.get_index_from_bit(player.position[1])


        if arg == 2:  # 'n'
            if player.position[0] > 0:
                temp_y0 += -1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]

                if self.unobstructed( terr ):
                    player.position[0] = player.position[0] - 1
                    # player.position[1] = player.position[1]
            else:

                self.current_map[0] += -1
                player.position[0] = self.MAP_SIZE - 1



        elif arg == 0:  # '0' :
            pass
            # player.position[0] = player.position[0]
            # player.position[1] = player.position[1]

        elif arg == 8:
            # 's' | '8' :
            if player.position[0] < 23:
                temp_y0 += 1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed( terr ):
                    player.position[0] = player.position[0] + 1
                    # player.position[1] = player.position[1]
            else:
                self.current_map[0] += 1
                player.position[0] = (player.position[0] + 1 ) % 24
        #          CHANGE MAP


        # move(8)

        elif arg == 6:  # 'w' | '6' :
            print(">w player.position[1] : ", player.position[1])
            if player.position[1] < 24:
                temp_x1 += 1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed( terr ):
                    player.position[1] = player.position[1] + 1
            # player.position[0] = player.position[0]

            else:
                self.current_map[1] += 1
                player.position[1] = 1

            # move(6)



        elif arg == 4:  # 'e' | '4' :

            print("<e player.position[1] : ", player.position[1])

            if player.position[1] > 1:
                temp_x1 += -1
                terrr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terrr):
                    player.position[1] = player.position[1] - 1
                    # player.position[0] = player.position[0]
            # move(4)

            else:
                self.current_map[1] += -1
                player.position[1] = 24



        #
        #
        # elif arg == 1:  # 'nw' | '1' :
        #     if player.position[0] > 0:
        #         temp_y0 += -1
        #         terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][ (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
        #         if self.unobstructed( terr ):
        #             player.position[0] = player.position[0] - 1
        #
        #     if player.position[1] < 1 << 23:
        #         temp_x1 += -1
        #         terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
        #                (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
        #         if self.unobstructed(terr):
        #             player.position[1] = player.position[1] << 1
        #     # move(1)
        #
        # elif arg == 3:  # 'ne' | '3' :
        #     if player.position[0] > 0:
        #         temp_y0 += -1
        #         terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][ (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
        #         if self.unobstructed( terr ):
        #             player.position[0] = player.position[0] - 1
        #     if player.position[1] > 1:
        #         temp_x1 += 1
        #         terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
        #                (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
        #         if self.unobstructed( terr ):
        #             player.position[1] = player.position[1] >> 1
        #     # move(3)
        #
        # elif arg == 7:  # 'sw' | '7' :
        #     if player.position[0] < 23:
        #         temp_y0 += 1
        #         terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
        #                (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
        #         if self.unobstructed( terr ):
        #             player.position[0] = player.position[0] + 1
        #     if player.position[1] < 1 << 23:
        #         temp_x1 += -1
        #         terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
        #                (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
        #         if self.unobstructed(terr):
        #             player.position[1] = player.position[1] << 1
        #     # move(7)
        #
        # elif arg == 9:  # 'se' | '9' :
        #     if player.position[0] < 23:
        #         temp_y0 += 1
        #         terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
        #                (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
        #         if self.unobstructed( terr ):
        #             player.position[0] = player.position[0] + 1
        #     if player.position[1] > 1:
        #         temp_x1 += 1
        #         terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
        #                (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
        #         if self.unobstructed( terr ):
        #             player.position[1] = player.position[1] >> 1
        #     # move(9)


        self.monster_go(player, monsters)
        # header(0)
        self.mapit(player, monsters)




