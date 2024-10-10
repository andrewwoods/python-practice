#
# Temperature
#
# A class to convert temperature to/from the Metric System
#


class Temperature:
    celsius_units = ["c", "celsius", "centigrade"]

    def celsius_to_farenheit(self, celsius):
        return (celsius * 1.8) + 32

    def run(self, quantity, units):
        if units.lower() in self.celsius_units:
            units = "C"
            result = float(self.celsius_to_farenheit(quantity))
            format = "Result: %0.2f %s is %0.2f F"
            print(format % (quantity, units, result))
            return
