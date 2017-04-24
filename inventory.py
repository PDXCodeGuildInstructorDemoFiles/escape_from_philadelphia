class Inventory:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.coin = 0
        self.inv = self.create_inv()
        self.weapon = None
        self.armor = None

    def __del__(self):
        "delete a thing"

    def create_inv(self, slots=15):
        dictionary = {}
        for i in range(1, slots + 1):
            dictionary[i] = None
        return dictionary

    def place_item(self, item):
        empty_slot = None
        for k, v in self.inv.items():
            if v is None:
                empty_slot = k
                break
        if empty_slot is not None:
            if self.weight - item.weight > 0:
                self.inv[empty_slot] = item
                self.weight -= item.weight
            else:
                print("too heavy")
        else:
            print("no empty")

    def print_inv(self):
        counter = 0
        for k, v in self.inv.items():
            if v is not None:
                print('{}: {}'.format(k, v))
                counter += 1
        if counter == 0:
            print('Bag is empty.')

    def console(self, player):
        # print(self.inv)
        while True:
            self.print_inv()
            print(player)
            # play_con = input("(U)se, (E)quip, (D)rop an item, (L)ook around you for an item, or (Q)uit?").lower()
            play_con = input("(U)se, (E)quip, (D)rop an item, or (Q)uit?").lower()
            if play_con == 'd':
                self.drop_item()
            elif play_con == 'q':
                break
            # elif play_con == 'l':
            #     self.look_for()
            elif play_con == 'u':
                self.use_item(player)
            elif play_con == 'e':
                self.equip_item()
                # self.place_item()

    # def look_for(self):
    #     # print(local_dict)
    #     pick_up = int(input("Which item do you want to pick up? "))
    #     self.place_item(local_dict[pick_up])
    #     # del local_dict[pick_up]
    #     print(self.inv)
    #     print(local_dict)

    def drop_item(self):
        print(self.inv)
        to_drop = int(input("which item do you want to drop?"))
        drop_val = self.inv[to_drop]
        # local_dict[to_dropd] = drop_val
        self.inv[to_drop] = None
        print(self.inv)
        # print(local_dict)

    def use_item(self, player):
        self.print_inv()
        to_use = int(input("which item do you want use?"))
        player.cls.hp += self.inv[to_use].effect
        self.inv[to_use] = None

    def equip_item(self):
        self.print_inv()
        eqp_itm = int(input("Which item do you want to equip? "))
        if 'weapon' in self.inv[eqp_itm].type.lower():
            removing = self.weapon
            self.weapon = self.inv[eqp_itm]
            self.inv[eqp_itm] = removing
            print('You have equipped {}'.format(self.weapon.name))

        elif 'armor' in self.inv[eqp_itm].type.lower():
            removing = self.armor
            self.armor = self.inv[eqp_itm]
            self.inv[eqp_itm] = removing
            print('You have equipped {}'.format(self.armor.name))
        else:
            print('That item can not be equipped!')

    def __str__(self):
        return self.inv
