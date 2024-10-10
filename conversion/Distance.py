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

    def run(self, quantity, units):
        if units == "km" or units == "kilometers":
            result = float(self.kilometers_to_miles(quantity))

            format = "Result: %0.2f %s is %0.2f miles"
            print(format % (quantity, units, result))
            return

        elif units == "mi" or units == "miles":
            result = float(self.miles_to_kilometers(quantity))

            format = "Result: %0.2f %s is %0.2f kilometers"
            print(format % (quantity, units, result))
            return
