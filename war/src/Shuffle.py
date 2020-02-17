import random 
from src.Deck import Deck 

class DeckShuffleStrategy: 
  def shuffleDeck(self, deck: Deck): 
    """ shuffles deck. Default implementation leaves deck as is """
    pass 

class SimpleShuffleStrategy(DeckShuffleStrategy): 
  def shuffleDeck(self, deck: Deck):
    """ shuffles deck """
    #:: remove all the cards from the deck. 
    cards = deck.popAll() 
    #:: shuffle the list. 
    random.shuffle(cards) 
    #:: put it pack in the deck. 
    deck.extend(cards)