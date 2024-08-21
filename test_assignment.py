import unittest
from assignment import generate_deck, card_name, hand_value

class TestBlackjack(unittest.TestCase):

    def test_generate_deck(self):
        deck = generate_deck()
        self.assertEqual(len(deck), 52)
        self.assertTrue(all(suit in 'cdhs' for card in deck for suit in card[-1]))
        self.assertTrue(all(1 <= int(card[:-1]) <= 13 for card in deck))

    def test_card_name(self):
        self.assertEqual(card_name('13h'), 'King of Hearts')
        self.assertEqual(card_name('1s'), 'Ace of Spades')
        self.assertEqual(card_name('3d'), '3 of Diamonds')

    def test_hand_value(self):
        self.assertEqual(hand_value(['1h', '13d', '7c']), 18)
        self.assertEqual(hand_value(['1h', '5d', '1c']), 17)  
    
if __name__ == "__main__":
    unittest.main()