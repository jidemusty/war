import unittest 
from src.Card import Card, Rank, Suite 

class CardTestCase(unittest.TestCase):
  def test_cardInitialization(self):
    """ tests that card is initialized properly """
    card = Card(Rank.ACE, Suite.HEART) 
    self.assertEqual(card._rank, Rank.ACE) 
    self.assertEqual(card._suite, Suite.HEART) 

  def test_getRankAndSuite(self):
    card = Card(Rank.ACE, Suite.HEART) 
    self.assertEqual(card.getRank(), Rank.ACE) 
    self.assertEqual(card.getSuite(), Suite.HEART) 

"""
python3 -m unittest discover -s test -p "test_*.py"
"""