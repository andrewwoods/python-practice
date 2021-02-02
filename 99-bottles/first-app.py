#
# 99 Bottles of Beer song
#
# Attempt #1
#

import first

quantity = input('How many bottles would you like? ')
quantity = int(quantity)

song = first.BottlesSong(quantity)
song.show_song_title_banner()
song.generate()
