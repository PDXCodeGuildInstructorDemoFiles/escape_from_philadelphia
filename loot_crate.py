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
        print('You have found an old world loot crate. The crate will allow you to take one item before it locks forever.')
        for k, v in self.contents.items():
            print(k, v)
        user_choice = int(input('Which number do you want?: '))
        print('You picked {}, good choice!'.format(self.contents[user_choice].name))
        return self.contents[user_choice]

class VendMachine:
    def __init__(self, location, lvl):
        self.location = location
        self.rewards = self.create_rewards(lvl)
        self.cost = 10

    def __str__(self):
        return '{}'.format(self.rewards)

    def __repr__(self):
        return '{}'.format(self.rewards)

    def create_rewards(self, lvl, slots=3):
        rewards = {}
        methods = [mil.create_weapon, mil.create_armor]
        for x in range(1, slots + 1):
            rewards[x] = (random.choice(methods)(lvl))
        return rewards

    def vend_interface(self):
        active = True
        coin = 100
        while active:
            play = input(
                "Welcome to the Loot'O'Matic vending machine! (B)uy, (S)ell, (E)xit: ").upper()
            if play == 'B':
                for k, v in self.rewards.items():
                    print('{}:{}'.format(k, v))
                rchoice = int(input('Look at those amazing choices. Which one do you want?: '))
                if coin >= self.rewards[rchoice].cost:
                    print('You take {}.'.format(self.rewards[rchoice].name))
                    coin -= self.rewards[rchoice].cost
                    print('You have ${} left.'.format(coin))
                    return self.rewards[rchoice]
                else:
                    print('You do not have enough money, haha!')
            elif play == 'S':

            else:g
                active = False

slot1 = VendMachine('here', 2)
slotif = slot1.vend_interface()
print(slotif)




#
# crate1 = LootCrate('Right here', 1)
# itemtake1 = crate1.take_one_item()
# print(itemtake1)