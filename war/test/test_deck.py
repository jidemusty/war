import unittest 
from src.Card import Card , Rank, Suite 
from src.Deck import Deck 

class DeckTestCase(unittest.TestCase):
  def test_constructor_initialization(self):
    """ test desck initialization """
    deck = Deck() 
    self.assertEqual(deck.isEmpty(), True) 


  def test_popTopCard_returnsNoneIfEmpty(self):
    deck  = Deck() 
    card = deck.popTopCard()
    self.assertEqual(card,None) 

  def test_isEmpty_returnsTrueIfEmtpy(self):
    deck = Deck()
    self.assertEqual(deck.isEmpty(),True) 

  def test_isEmptyReturnsFalseIfNotEmpty(self):
    deck = Deck()
    deck.pushToTop(Card(Rank.ACE,Suite.HEART))
    self.assertEqual(deck.isEmpty(),False)

  def test_size_returnsZeroIfEmpty(self):
    deck = Deck() 
    self.assertEqual(deck.size(),0) 
    #:: add some items. 

  def test_size_returnsNonZeroIfNotEmpty(self):
    deck = Deck()
    cards = [Card(Rank.ACE,Suite.HEART), Card(Rank.TWO,Suite.PIKES)]
    deck.pushToTop(cards[0])
    deck.pushToTop(cards[1])
    self.assertEqual(deck.size(),2)

  def test_pushToTop_pushesCardToTopOfDeck(self):
    deck = Deck() 
    #:: create some cards 
    cards = [Card(Rank.ACE,Suite.HEART), Card(Rank.TWO,Suite.PIKES)]
    deck.pushToTop(cards[0])
    deck.pushToTop(cards[1])
    #:: verify 
    self.assertEqual(deck.popTopCard(),cards[1])
    self.assertEqual(deck.popTopCard(),cards[0])

  def test_pushToBottom_pushesCardToBottomOfDeck(self):
    deck = Deck() 
      #:: create some cards 
    cards = [Card(Rank.ACE,Suite.HEART), Card(Rank.TWO,Suite.PIKES)]
    deck.pushToBottom(cards[0])
    deck.pushToBottom(cards[1])
    #:: verify 
    self.assertEqual(deck.popTopCard(),cards[0])
    self.assertEqual(deck.popTopCard(),cards[1])

  def test_popAll_returnsEmptyIterableIfEmpty(self):
    deck = Deck() 
    cards  = deck.popAll()
    self.assertEqual(len(cards),0)

  def test_popAll_returnsIterableIfNonEmpty(self):
    deck = Deck() 
    #:: insert some cards. 
    cards = [Card(Rank.ACE,Suite.HEART), Card(Rank.TWO,Suite.PIKES)]
    deck.pushToBottom(cards[0])
    deck.pushToBottom(cards[1])

    result = deck.popAll() 
    self.assertEqual(deck.size(),0) #:: must be empty
    self.assertEqual(deck.isEmpty(),True)
    self.assertEqual(len(result),2) 

    #:: verify items match 

    self.assertEqual(cards[0],result[0]) 
    self.assertEqual(cards[1],result[1])


  def test_extend_extendsDeckByIterable(self):
    deck1 = Deck() 
    cards1 = [Card(Rank.ACE,Suite.HEART), Card(Rank.TWO,Suite.PIKES)]
    deck1.pushToBottom(cards1[0])
    deck1.pushToBottom(cards1[1])

    deck2 = Deck() 
    cards2 = [Card(Rank.JACK,Suite.HEART), Card(Rank.THREE,Suite.PIKES)]
    deck2.pushToBottom(cards2[0])
    deck2.pushToBottom(cards2[1])
    #:: extend deck2 
    popped1 = deck1.popAll()
    deck2.extend(popped1)
    #:: asserts 
    self.assertEqual(deck2.size(),4) 
    #:: verify the contens of deck2 mach. 
    popped2 = deck2.popAll() 
    self.assertEqual(popped2[0],cards2[0])
    self.assertEqual(popped2[1],cards2[1])
    self.assertEqual(popped2[2],cards1[0])
    self.assertEqual(popped2[3],cards1[1])


