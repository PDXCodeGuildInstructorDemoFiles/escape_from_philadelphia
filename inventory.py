import random

class Items:
    def __init__(self, name, type, effect, weight):                                                                     #added Items code for testing purposes.
        self.name = name                                                                                                #Chris says we can import it like a module
        self.type = type
        self.effect = effect
        self.weight = weight

    def __str__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.effect, self.weight)
    def __repr__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.effect, self.weight)

def weapon(effect):
    w_names = ['sword of might', 'wooden sword', 'big axe', 'dagger']
    return Items(random.choice(w_names), 'weapon', effect, random.randrange(5, 10))

sword = weapon(-20)

class Inventory:                                                                                                        #create inv class                                                                                             #things on the gound

    def __init__(self, name, type, weight):                                                                             #inventory organization scheme
        self.name = name
        self.type = type
        self.weight = weight
        self.inventory = {}
    def __str__(self):                                                                                                  #str method for display
        return 'Name: {} Type: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.weight)
    def __repr__(self):
        return 'Name: {} Type: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.weight)

    def add_item(self, item):                                                                                                     #picking up/adding an item.
        # up_item = input("You come across a {} on the ground. Do you want to pick it up? \(Y\)es or \(N\)o?: ").format(self.local_item).upper()
        # if up_item == "Y":
              if bag_slots +1 > 10:
                  print("Bag is full!")

              elif bag_weight < 100:
                  print("Bag will be too heavy! Can't add this!")
              else:
                  #add-to-inventory function here


        #     player_inv.append(self.local_item)
        #     print("You picked up the {}.").format(self.local_item)                                                      #all for shit
        # elif up_item == "N":
        #     print("You leave the {} where it lies.").format(self.local_item)
         self.inventory[+1] = item                #no earthly idea what this means (why does the second item in the inventory need a variable?)    #may need to create method for trade/purchase

def use_item(self):#more bullshit to follow
    use_response = input("Do you want to V(iew) your")

    print player_inv
    player_inv[position]

    pass


def enable_item(self):
    pass


def list_item(self):
    pass




weapon = Items("sword", "weapon", 20, 5)                                                                                #hard coded shit.
inv = Inventory("inventory", "stuff", 500)
inv.add_item(weapon)
print(inv.inventory)