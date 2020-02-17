
from src.Game import Game 
from src.Deck import Deck 
from src.Shuffle import SimpleShuffleStrategy
from src.Card import Card, Rank, Suite , RankScore

"""
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
"""

def createPlayingDeck(suites: List[Suite], ranks: List[Rank]) -> Deck:
  deck = Deck() 
  for rank in ranks :
    for suite in suites:
      card = Card(rank,suite)
      deck.pushToTop(card) 

  return deck 


def main():
  suites = [Suite.HEART,Suite.TILES] #::TODO add all the suites. 
  ranks  = [Rank.ACE,Rank.Jack] 
  initial_deck = createPlayingDeck(suites, ranks) 

  #:: create a list of players. 

  #:: create your shuffle strategy 

  #:: create your ranking strategy 

  #:: create game

  #:: call game.start() 


  pass 


main() 