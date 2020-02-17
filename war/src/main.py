from src.Game import Game 
from src.Deck import Deck 
from src.Shuffle import SimpleShuffleStrategy
from src.Card import Card, Rank, Suite , RankScore

def createPlayingDeck(suites: List[Suite], ranks: List[Rank]) -> Deck:
  deck = Deck() 
  for rank in ranks:
    for suite in suites:
      card = Card(rank, suite)
      deck.pushToTop(card) 

  return deck 


def main():
  suites = [Suite.HEART, Suite.TILES, Suite.CLOVERS, Suite.PIKES] 
  ranks  = [
    Rank.ACE, Rank.KING, Rank.QUEEN, Rank.JACK,
    Rank.TEN, Rank.NINE, Rank.EIGHT, Rank.SEVEN,
    Rank.SIX, Rank.FIVE, Rank.FOUR, Rank.THREE,
    Rank.TWO
  ]
  
  initial_deck = createPlayingDeck(suites, ranks) 

  #:: create a list of players. 

  #:: create your shuffle strategy 

  #:: create your ranking strategy 

  #:: create game

  #:: call game.start() 


  pass 


main() 