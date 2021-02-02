"""
First attempt
"""
class BottlesSong:

    def __init__(self, quantity):
        self.quantity = quantity
        self.starting_quantity = quantity

    def show_song_title_banner(self):
        title = str(self.starting_quantity) + " bottles of beer"
        print()
        print(title.upper())
        print()

    def generate(self):
        while self.quantity >= 0:
            if self.quantity == 0:
                self.create_0_bottle_verse(self.quantity)
            elif self.quantity == 1:
                self.create_1_bottle_verse(self.quantity)
            elif self.quantity == 2:
                self.create_2_bottle_verse(self.quantity)
            else:
                self.create_verse(self.quantity)

    def create_0_bottle_verse(self, quantity):
        print("No more bottles of beer on the wall, ")
        print("No more bottles of beer")
        print("Go to the store, and buy some more")
        print(str(self.starting_quantity) + " bottles of beer on the wall\n")

        self.quantity -= 1


    def create_1_bottle_verse(self, quantity):
        print(str(quantity) + " bottle of beer on the wall, ")
        print(str(quantity) + " bottle of beer")
        print("Take one down, pass it around")
        quantity -= 1
        print("No more bottles of beer on the wall\n")

        self.quantity = quantity

    def create_2_bottle_verse(self, quantity):
        print(str(quantity) + " bottles of beer on the wall, ")
        print(str(quantity) + " bottles of beer")
        print("Take one down, pass it around")
        quantity -= 1
        print("1 bottle of beer on the wall\n")

        self.quantity = quantity

    def create_verse(self, quantity):
        print(str(quantity) + " bottles of beer on the wall, ")
        print(str(quantity) + " bottles of beer")
        print("Take one down, pass it around")
        quantity -= 1
        print(str(quantity) + " bottles of beer on the wall\n")

        self.quantity = quantity

