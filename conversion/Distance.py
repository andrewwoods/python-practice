#
#
#

# Perform a variety of distance-related methods.
class Distance:
    def kilometers_to_miles(self, km):
        factor = 0.621371

        return km * factor

    def run(self):
        distance = input("What distance would you like to convert? ")

        if distance.find("km") or distance.find("kilometers"):
            amount = float(input("how many? "))
            result = float(self.kilometers_to_miles(amount))

            format = "Result: %0.2f %s is %0.2f miles"
            print(format % (amount, distance, result))
