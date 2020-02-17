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


class RankScore: 
  SCORES = {Rank.ACE: 14, 
           Rank.KING : 13, 
           Rank.QUEEN: 12,
           Rank.JACK: 11,
           Rank.TEN: 10,
           Rank.NINE: 9,
           Rank.EIGHT: 8,
           Rank.SEVEN: 7, 
           Rank.SIX: 6, 
           Rank.FIVE: 5, 
           Rank.FOUR: 4,
           Rank.THREE: 3, 
           Rank.TWO: 2, 
           }
  def getScore(self, rank: Rank): 
    """ returns the rank score for the card """ 
    return  self.SCORES[rank] 


  


class Card:
  """ @class Card: class representation of a card """
  def __init__(self, rank: Rank , suite: Suite):
    self._rank = rank
    self._suite = suite
  
  def getSuite(self) -> Suite:
    return self._suite

  def getRank(self) -> Rank:
    return self._rank

  def __eq__(self,other: 'Card') -> bool:
    """ compare if two cards are equal """ 
    return (self.getRank() == other.getRank() and self.getSuite() == other.getSuite())

