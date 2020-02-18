from src.Game import Game 
from src.Deck import Deck 
from src.Player import Player
from src.utils import createPlayingDeck
from src.Shuffle import SimpleShuffleStrategy
from src.Card import Card, Rank, Suite, RankScore

def main():
  #:: for a longer game play(longer because of the number of cards in deck), 
  # uncomment and use this input below
  
  # suites = [Suite.HEART, Suite.TILES, Suite.CLOVERS, Suite.PIKES] 
  # ranks  = [
  #   Rank.ACE, Rank.KING, Rank.QUEEN, Rank.JACK,
  #   Rank.TEN, Rank.NINE, Rank.EIGHT, Rank.SEVEN,
  #   Rank.SIX, Rank.FIVE, Rank.FOUR, Rank.THREE,
  #   Rank.TWO
  # ]
  # initial_deck = createPlayingDeck(suites, ranks)
  
  initial_deck_list = [
    Card(Rank.ACE, Suite.HEART),
    Card(Rank.ACE, Suite.CLOVERS),
    Card(Rank.ACE, Suite.PIKES),
    Card(Rank.TWO, Suite.CLOVERS)
  ]

  initial_deck = Deck()
  initial_deck.extend(initial_deck_list)

  #:: create a list of players.
  player_one = Player("Mario", Deck())
  player_two = Player("Luigi", Deck())
  players = [player_one, player_two]

  #:: create your shuffle strategy
  shuffleStrategy = SimpleShuffleStrategy() 

  #:: create your ranking strategy 
  rankingStrategy = RankScore()

  #:: create game
  game = Game(initial_deck, players, shuffleStrategy, rankingStrategy)

  #:: call game.start()
  game.start()

main() 