from src.Card import Card 

from collections import deque 
from typing import List, Iterable

class Deck: 
  """@class Deck: Manages a card deck  """
  def __init__(self):
    self._cards = deque()
    #:: top(left) bottom(right) 

  def pushToTop(self, card: Card):
    """ adds card to the top of the deck"""
    self._cards.appendleft(card)

  def pushToBottom(self, card: Card):
    """ adds card to the bottom of the deck """
    self._cards.append(card)

  def isEmpty(self) -> bool:
    """ returns true if deck is empty or false otherwise """
    return self.size() == 0 

  def popTopCard(self) -> Card: 
    """ pops the the card at the top of the desk and returns it if non empy, or None. 
        return:
          Card or None 
    """
    return self._cards.popleft() if not self.isEmpty() else None 

  def popAll(self) -> Iterable[Card]: 
    """ pops all cards from current deck 
    return :
      Iterable of Card 
    """
    tmp = self._cards 
    self._cards = [] 
    return tmp  

  def extend(self, cards: Iterable[Card]):
    """ extends the current deck by appending all cards in @param deck into the curent deck"""
    self._cards.extend(cards)

  def size(self) -> int:
    return len(self._cards) 


