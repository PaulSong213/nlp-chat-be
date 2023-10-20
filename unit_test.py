import unittest

class TestCorrectZarateTerm(unittest.TestCase):

    def test_correction(self):
        from chatterbot.conversation import Statement
        from preprocessors import correct_zarate_term 

        # Test case 1: Single word correction
        statement1 = Statement("Zarate is a place.")
        corrected1 = correct_zarate_term(statement1)
        self.assertEqual(corrected1.text, "E. Zarate Hospital is a place.")

        # Test case 2: Multiple corrections in a sentence
        statement2 = Statement("Zarate Hospital is a great place. Hospital staff is friendly.")
        corrected2 = correct_zarate_term(statement2)
        self.assertEqual(corrected2.text, "E. Zarate Hospital is a great place. E. Zarate Hospital staff is friendly.")

        # Test case 3: Only hospital
        statement3 = Statement("The Hospital provides excellent service.")
        corrected3 = correct_zarate_term(statement3)
        self.assertEqual(corrected3.text, "The E. Zarate Hospital provides excellent service.")

if __name__ == '__main__':
    unittest.main()
