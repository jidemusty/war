import unittest 
from src.Player import Player 
from src.Card import Card, Suite, Rank
from src.Deck import Deck 

class PlayerTestCase(unittest.TestCase):
  def test_player_constructor(self):
    deck = Deck()
    player = Player("Mustapha", deck)
    self.assertEqual(player.getName(), "Mustapha")
    self.assertEqual(player._deck, deck)
  
  def test_empty_deck(self):
    deck = Deck()
    player = Player("Mustapha", deck)
    self.assertEqual(player.isDeckEmpty(), True)

  def test_player_deck(self):
    deck = Deck()
    player = Player("Mustapha", deck)
    #::
    cards = [Card(Rank.ACE, Suite.HEART), Card(Rank.TWO, Suite.PIKES)]
    player.addToDeckBottom(cards)

    self.assertEqual(player.popDeckTopCard(), cards[0])
    self.assertEqual(player.popDeckTopCard(), cards[1])