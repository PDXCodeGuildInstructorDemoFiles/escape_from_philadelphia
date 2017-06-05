from char import Character
from loot_crate import LootCrate
from monster import Monster
import os

#this is a chagge
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Map:
    def __init__(self, name, map_size=24):
        self.name = name
        self.map_size = map_size
        self.map = self.create_grid()
        self.message = ''

    def add_message(self, message):
        if len(self.message) > 0:
            self.message += '\n' + message
        else:
            self.message = message

    def create_grid(self):
        map_dict = {}
        for i in range(self.map_size):
            for y in range(self.map_size):
                key = (i, y)
                map_dict[key] = MapObject('none', ' .. ', True)
        return map_dict

    def open_crate(self, player):
        dir_dict = {
            'n': (player.location[0] - 1, player.location[1]),
            's': (player.location[0] + 1, player.location[1]),
            'e': (player.location[0], player.location[1] + 1),
            'w': (player.location[0], player.location[1] - 1)
        }
        if dir_dict['n'] in self.map and self.map[dir_dict['n']].name == 'LootCrate':
            if not self.map[dir_dict['n']].looted:
                crate = self.map[dir_dict['n']]
                player.inv.place_item(crate.take_one_item())
                crate.looted = True
                crate.avatar = ' 🗃  '
            else:
                self.add_message('This has already been looted.')
        elif dir_dict['e'] in self.map and self.map[dir_dict['e']].name == 'LootCrate':
            if not self.map[dir_dict['e']].looted:
                crate = self.map[dir_dict['e']]
                player.inv.place_item(crate.take_one_item())
                crate.looted = True
                crate.avatar = ' 🗃  '
            else:
                self.add_message('This has already been looted.')
        elif dir_dict['s'] in self.map and self.map[dir_dict['s']].name == 'LootCrate':
            if not self.map[dir_dict['s']].looted:
                crate = self.map[dir_dict['s']]
                player.inv.place_item(crate.take_one_item())
                crate.looted = True
                crate.avatar = ' 🗃  '
            else:
                self.add_message('This has already been looted.')
        elif dir_dict['w'] in self.map and self.map[dir_dict['w']].name == 'LootCrate':
            if not self.map[dir_dict['w']].looted:
                crate = self.map[dir_dict['w']]
                player.inv.place_item(crate.take_one_item())
                crate.looted = True
                crate.avatar = ' 🗃  '
            else:
                self.add_message('This has already been looted.')
        else:
            self.add_message('There is nothing to loot here!')

    def check_move(self, object, direction):
        """
        :param object: Game Object 
        :param direction: Cardinal Direction 
        :return: Move object if move is possible, return true or false and location information for messaging.
        """

        dir_dict = {
            'n': (object.location[0] - 1, object.location[1]),
            's': (object.location[0] + 1, object.location[1]),
            'e': (object.location[0], object.location[1] + 1),
            'w': (object.location[0], object.location[1] - 1)
        }

        if direction == 'n' and dir_dict['n'][0] >= 0 and (
                        self.map[dir_dict['n']] is None or self.map[dir_dict['n']].traversable):
            self.move(player, dir_dict['n'])
            return True, dir_dict['n']
        elif direction == 's' and dir_dict['s'][0] < self.map_size and (
                        self.map[dir_dict['s']] is None or self.map[dir_dict['s']].traversable):
            self.move(player, dir_dict['s'])
            return True, dir_dict['s']
        elif direction == 'e' and dir_dict['e'][1] < self.map_size and (
                        self.map[dir_dict['e']] is None or self.map[dir_dict['e']].traversable):
            self.move(player, dir_dict['e'])
            return True, dir_dict['e']
        elif direction == 'w' and dir_dict['w'][1] >= 0 and (
                        self.map[dir_dict['w']] is None or self.map[dir_dict['w']].traversable):
            self.move(player, dir_dict['w'])
            return True, dir_dict['w']
        else:
            return False, dir_dict[direction]

    def move(self, object, coord):
        """
        Moved item to desired location
        :param object: Object to be moved 
        :param coord: Coordinates object will move to
        """
        self.map[coord] = object
        self.map[object.location] = MapObject('none', '    ', True)
        object.location = coord

    def render(self):
        """
        Print to console map and all things on map.
        :return: 
        """
        for l in range(self.map_size):
            line = ''
            for k, v in self.map.items():
                if k[0] == l:
                    line += v.avatar
            print(line)


class MapObject:
    def __init__(self, name, avatar, traversable):
        self.name = name
        self.avatar = avatar
        self.traversable = traversable


map1 = Map('Area 1')
vert_wall = MapObject('wall', ' || ', False)
hors_wall = MapObject('wall', '====', False)
vert_wall_t = MapObject('wall', ' ||=', False)
hors_wall_l = MapObject('wall', '=== ', False)
map1.map[(0, 0)] = vert_wall
map1.map[(1, 0)] = vert_wall_t
map1.map[(2, 0)] = vert_wall
map1.map[(3, 0)] = vert_wall
map1.map[(4, 0)] = vert_wall
map1.map[(5, 0)] = vert_wall
map1.map[(6, 0)] = vert_wall
map1.map[(7, 0)] = vert_wall
map1.map[(8, 0)] = vert_wall
map1.map[(9, 0)] = vert_wall
map1.map[(10, 0)] = vert_wall
map1.map[(11, 0)] = vert_wall
map1.map[(12, 0)] = vert_wall
player = Character('Chris')
map1.map[(0, 1)] = player
map1.map[(1, 1)] = hors_wall
map1.map[(1, 2)] = hors_wall
map1.map[(1, 3)] = hors_wall
map1.map[(1, 5)] = hors_wall
map1.map[(1, 6)] = hors_wall_l
map1.map[(0, 6)] = vert_wall
map1.map[(0, 5)] = LootCrate((0, 5), 1)
map1.map[(12, 12)] = Monster()
map1.map[(12, 12)].generate_monster(1)
# print(map1.map[(12, 12)])
# print(map1.check_move((0, 1), 'n'))
# print(map1.check_move((0, 1), 'e'))
# print(map1.check_move((0, 1), 's'))
# print(map1.check_move((0, 1), 'w'))
#
while True:
    cls()
    map1.render()
    if len(map1.message) > 0:
        print(map1.message)
        map1.message = ''
    q = input('What direction would you like to move? ').lower()
    if q == 'n':
        mv = map1.check_move(player, 'n')
        if not mv[0]:
            try:
                map1.add_message("Can't move here, there is a {} in the way!".format(map1.map[mv[1]].name))
            except KeyError:
                map1.add_message("Can't move here, that's the edge of the map!")
    elif q == 'e':
        mv = map1.check_move(player, 'e')
        if not mv[0]:
            try:
                map1.add_message("Can't move here, there is a {} in the way!".format(map1.map[mv[1]].name))
            except KeyError:
                map1.add_message("Can't move here, that's the edge of the map!")
    elif q == 's':
        mv = map1.check_move(player, 's')
        if not mv[0]:
            try:
                map1.add_message("Can't move here, there is a {} in the way!".format(map1.map[mv[1]].name))
            except KeyError:
                map1.add_message("Can't move here, that's the edge of the map!")
    elif q == 'w':
        mv = map1.check_move(player, 'w')
        if not mv[0]:
            try:
                map1.add_message("Can't move here, there is a {} in the way!".format(map1.map[mv[1]].name))
            except KeyError:
                map1.add_message("Can't move here, that's the edge of the map!")
    elif 'open' in q:
        map1.open_crate(player)
    else:
        map1.add_message('I did not understand that.')
