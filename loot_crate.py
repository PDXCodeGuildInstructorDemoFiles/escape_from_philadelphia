import master_items_list as mil
import random


class LootCrate:
    def __init__(self, location, lvl):
        self.location = location
        self.contents = self.create_contents(lvl)

    def __str__(self):
        return '{}'.format(self.contents)

    def __repr__(self):
        return '{}'.format(self.contents)

    def create_contents(self, lvl, slots=10):
        contents = {}
        methods = [mil.create_weapon, mil.create_armor, mil.create_first_aid]
        for x in range(1, slots + 1):
            contents[x] = random.choice(methods)(lvl)
        return contents

    def take_one_item(self):
        print('You have found an old world loot crate. The crate will allow you to take on item before it locks forever.')
        for k, v in self.contents.items():
            print(k, v)
        user_choice = int(input('Which number do you want?: '))
        print('You picked up a {}, good choice.'.format(self.contents[user_choice].name))
        return self.contents[user_choice]



crate1 = LootCrate('Right here', 1)
itemtake1 = crate1.take_one_item()
print(itemtake1)