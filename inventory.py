class Inventory:

    def __init__(self, position, name, type, weight):
        self.position = position
        self.name = name
        self.type = type
        self.weight = weight
        self.coin = 0

    def __str__(self):
        return 'Position  Name    Type    Weight  \n     {}    {}    {}     {}   '.format(self.position, self.name, self.type, self.weight)
        return str(char_inv)
    # def __repr__(self):
    #     return str(char_inv)

    def use_item(self):










char_inv = []
knife = Inventory(1,"knife","wep",5)
gun = Inventory(2, "gun", "wep", 1)

char_inv.append(gun)
char_inv.append(knife)
for x in char_inv:
    print(x)
