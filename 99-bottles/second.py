class BottleSong:
    def __init__(self, quantity):
        self.quantity = quantity

    def generate(self):
        quantity = self.quantity
        while (quantity >= 0):
            print(self.verse(quantity))
            quantity -= 1

    def verse(self, quantity):
        output = self.number_of_bottles(quantity) + ' on the wall\n'
        output += self.number_of_bottles(quantity) + '\n'
        output += self.action(quantity)
        quantity -= 1
        output += self.number_of_bottles(quantity) + ' on the wall\n'

        return output

    def action(self, quantity):
        output = ''
        if quantity == 0:
            output += 'Go to the store, buy some more\n'
        elif quantity == 1:
            output += 'take it down, pass it around\n'
        else:
            output += 'take one down, pass it around\n'

        return output

    def number_of_bottles(self, quantity):
        if quantity == 6:
            return '6-pack of beer' 

        if quantity == 1:
            return str(quantity) + ' bottle of beer' 

        if quantity == 0:
            return 'No more bottles of beer' 

        if quantity == -1:
            return str(self.quantity) + ' bottles of beer' 

        return str(quantity) + ' bottles of beer' 
