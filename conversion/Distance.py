#
#
#

# Perform a variety of distance-related methods.
class Distance:
    def kilometers_to_miles(self, km):
        factor = 0.621371

        return km * factor

    def miles_to_kilometers(self, mi):
        factor = 0.621371

        return mi / factor

    def run(self):
        distance = input("What distance would you like to convert? ")

        if distance == "km" or distance == "kilometers":
            amount = float(input("how many kilometers? "))
            result = float(self.kilometers_to_miles(amount))

            format = "Result: %0.2f %s is %0.2f miles"
            print(format % (amount, distance, result))
            return

        elif distance == "mi" or distance == "miles":
            amount = float(input("how many miles? "))
            result = float(self.miles_to_kilometers(amount))

            format = "Result: %0.2f %s is %0.2f kilometers"
            print(format % (amount, distance, result))
            return
