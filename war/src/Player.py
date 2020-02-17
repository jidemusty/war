from src.Deck import Deck 
from src.Card import Card 
from typing import Iterable  

class Player:
  """@class Player: Manages a card deck  """
  def __init__(self, name: str, deck: Deck):
    self._name = name
    self._deck = None 
    self.setDeck(deck) 

  def getId(self):
    return self._name 

  def setDeck(self,deck: Deck): 
    self._deck = deck 

  def getDeckTopCard(self) -> Card: 
    return self._deck.getCardOnTop() 

  def isDeckEmpty(self):
    return self._deck.isDeckEmpty() 

  def addToDeckBottom(self, cards: Iterable[Card]):
    """ adds the list of cards to bottom of deck """
    self._deck.extend(cards)

  
