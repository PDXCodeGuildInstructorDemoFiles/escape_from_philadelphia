class Inventory:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.coin = 0
        self.inv = self.create_inv()

    def create_inv(self, slots=15):
        dictionary = {}
        for i in range(1, slots + 1):
            dictionary[i] = 'empty'
        return dictionary

    def __str__(self):
        return self.inv
        # return 'Position  Name    Type    Weight  \n     {}    {}    {}     {}   '.format(self.position, self.name, self.type, self.weight)
    # def __repr__(self):
    #     return str(char_inv)

    # def use_item(self):

inventory = Inventory('player bags', 50)
print(inventory.inv)


# char_inv = []
# knife = Inventory(1,"knife","wep",5)
# gun = Inventory(2, "gun", "wep", 1)
#
# char_inv.append(gun)
# char_inv.append(knife)
# for x in char_inv:
#     print(x)
