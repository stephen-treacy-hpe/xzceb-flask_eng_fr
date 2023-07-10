import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test_english_to_french(self): 
        french_text = english_to_french("hello")
        self.assertEqual(french_text, "bonjour")

        

class TestFrenchToEnglish(unittest.TestCase): 
    def test_french_to_english(self): 
        english_text = french_to_english("bonjour")
        self.assertEqual(english_text, "hello")

unittest.main()