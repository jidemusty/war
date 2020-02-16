from enum import Enum 

class Suite(Enum): 
  HEART = 'HEART'
  TILES = 'TILES'
  CLOVERS = 'CLOVERS'
  PIKES = 'PIKES'

class Rank(Enum):
  ACE = 'ACE'
  KING = 'KING'
  QUEEN = 'QUEEN'
  JACK = 'JACK'
  TEN = '10'
  NINE = '9'
  EIGHT = '8'
  SEVEN = '7'
  SIX = '6'
  FIVE = '5'
  FOUR = '4'
  THREE = '3'
  TWO = '2'


class Card:
  """ @class Card: class representation of a card """
  def __init__(self, rank: Rank , suite: Suite):
    self._rank = rank
    self._suite = suite
  
  def getSuite(self):
    return self._suite

  def getRank(self):
    return self._rank

