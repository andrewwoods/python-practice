import unittest
import second

class TestSecond(unittest.TestCase):

    def test_first_verse(self):
        expected = "99 bottles of beer on the wall\n"
        expected += "99 bottles of beer\n"
        expected += "take one down, pass it around\n"
        expected += "98 bottles of beer on the wall\n"

        song = second.BottleSong(99)
        
        response = song.verse(99)

        self.assertEqual(expected, response)
   
    def test_50_verse(self):
        expected = "50 bottles of beer on the wall\n"
        expected += "50 bottles of beer\n"
        expected += "take one down, pass it around\n"
        expected += "49 bottles of beer on the wall\n"

        song = second.BottleSong(99)
        
        response = song.verse(50)

        self.assertEqual(expected, response)
    
    def test_6_verse(self):
        expected = "6-pack of beer on the wall\n"
        expected += "6-pack of beer\n"
        expected += "take one down, pass it around\n"
        expected += "5 bottles of beer on the wall\n"

        song = second.BottleSong(99)
        
        response = song.verse(6)

        self.assertEqual(expected, response)
    
    def test_3_verse(self):
        expected = "3 bottles of beer on the wall\n"
        expected += "3 bottles of beer\n"
        expected += "take one down, pass it around\n"
        expected += "2 bottles of beer on the wall\n"

        song = second.BottleSong(99)
        
        response = song.verse(3)

        self.assertEqual(expected, response)
    
    def test_2_verse(self):
        expected = "2 bottles of beer on the wall\n"
        expected += "2 bottles of beer\n"
        expected += "take one down, pass it around\n"
        expected += "1 bottle of beer on the wall\n"

        song = second.BottleSong(99)
        
        response = song.verse(2)

        self.assertEqual(expected, response)
    
    def test_1_verse(self):
        expected = "1 bottle of beer on the wall\n"
        expected += "1 bottle of beer\n"
        expected += "take it down, pass it around\n"
        expected += "No more bottles of beer on the wall\n"

        song = second.BottleSong(99)
        
        response = song.verse(1)

        self.assertEqual(expected, response)
    
    def test_0_verse(self):
        expected = "No more bottles of beer on the wall\n"
        expected += "No more bottles of beer\n"
        expected += "Go to the store, buy some more\n"
        expected += "99 bottles of beer on the wall\n"

        song = second.BottleSong(99)
        
        response = song.verse(0)

        self.assertEqual(expected, response)
    
    def test_number_of_bottles(self):

        song = second.BottleSong(99)

        response = song.number_of_bottles(99)
        self.assertEqual('99 bottles of beer', response)

        response = song.number_of_bottles(3)
        self.assertEqual('3 bottles of beer', response)

        response = song.number_of_bottles(2)
        self.assertEqual('2 bottles of beer', response)

        response = song.number_of_bottles(1)
        self.assertEqual('1 bottle of beer', response)

        response = song.number_of_bottles(0)
        self.assertEqual('No more bottles of beer', response)

