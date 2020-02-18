from src.Deck import Deck 
from src.Card import Card 
from typing import Iterable  

class Player:
  """@class Player: Manages a card deck  """
  def __init__(self, name: str, deck: Deck):
    self._name = name
    self._deck = None 
    self.setDeck(deck) 

  def getDeckSize(self):
    return self._deck.size() 

  def getName(self):
    return self._name 

  def setDeck(self, deck: Deck): 
    self._deck = deck 

  def popDeckTopCard(self) -> Card: 
    """ pop the card at the top of the player's deck and returns it """
    return self._deck.popTopCard() 

  def isDeckEmpty(self):
    return self._deck.isEmpty() 

  def addToDeckBottom(self, cards: Iterable[Card]):
    """ adds the list of cards to bottom of deck """
    self._deck.extend(cards)

  def printDeck(self):
    deck_str = str(self._deck)
    print("[{}]: {}".format(self.getName(), deck_str))

  def __str__(self):
    return self.getName() 
