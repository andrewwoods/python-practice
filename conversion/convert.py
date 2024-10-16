#!/usr/bin/env python3
#
# convert.py
#
# This is a command line application convert different types of values.
#

import argparse
from Distance import Distance
from temperature import Temperature


def main():
    parser = argparse.ArgumentParser(
        prog="convert",
        description="An exercise to learn to create Python CLI applications",
        epilog="by Andrew Woods",
        usage="",
    )

    parser.add_argument("type")
    parser.add_argument("quantity")
    parser.add_argument("units")

    args = parser.parse_args()

    if args.type is None:
        parser.print_help()
    else:
        converter = get_converter(args.type)
        converter.run(float(args.quantity), args.units)


#
# This function returns an object with a run method.
#
# Each run method will hand off the program logic, that I import will
# have a run method. In PHP, I would use and interface to ensure that
# the run method exists. Python doesn't seem have an interface.
#
def get_converter(app_type):
    if app_type == "distance":
        return Distance()
    elif app_type == "temperature":
        return Temperature()
    else:
        message = "You have chosen poorly."
        message += 'Use "distance" as an argument on the command line.'
        raise RuntimeError(message)


if __name__ == "__main__":
    main()
