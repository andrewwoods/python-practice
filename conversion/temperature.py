#
# Temperature
#
# A class to convert temperature to/from the Metric System
#


class Temperature:
    celsius_units = ["c", "celsius", "centigrade"]

    # NOTE: Include farenheit as a common misspelling to help the user.
    fahrenheit_units = ["f", "fahrenheit", "farenheit"]

    def celsius_to_farenheit(self, celsius):
        return (celsius * 1.8) + 32

    def farenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) / 1.8

    def run(self, quantity, units):
        if units.lower() in self.celsius_units:
            units = "C"
            result = float(self.celsius_to_farenheit(quantity))
            format = "Result: %0.2f %s is %0.2f F"
            print(format % (quantity, units, result))
            return

        if units.lower() in self.fahrenheit_units:
            units = "F"
            result = float(self.farenheit_to_celsius(quantity))
            format = "Result: %0.2f %s is %0.2f C"
            print(format % (quantity, units, result))
            return
