#
# 99 Bottles of Beer song
#
# Attempt #2
#
# This uses testing with the Red, Green, Refactor approach
#

import second

quantity = input('How many bottles would you like? ')
quantity = int(quantity)

song = second.BottleSong(quantity)
title = str(quantity) + ' bottles of beer'
print(title.upper())
print()
song.generate()