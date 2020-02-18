import unittest 
from src.Game import Game, GameStatus
from src.Deck import Deck
from src.utils import createPlayingDeck
from src.Player import Player
from src.Shuffle import SimpleShuffleStrategy
from src.Card import Card, Rank, Suite, RankScore

class GameTestCase(unittest.TestCase):
  def setUp(self):
    suites = [Suite.HEART, Suite.TILES] 
    ranks  = [
      Rank.ACE, Rank.KING,
    ]

    self.initial_deck = createPlayingDeck(suites, ranks) 

    player_one = Player("Mario", Deck())
    player_two = Player("Luigi", Deck())
    self.players = [player_one, player_two]

    self.shuffle_strategy = SimpleShuffleStrategy() 
    self.ranking_strategy = RankScore()

  def test_game_constructor(self):
    game = Game(self.initial_deck, self.players, self.shuffle_strategy, self.ranking_strategy)

    self.assertEqual(game._playing_deck, self.initial_deck)
    self.assertEqual(game._current_play_deck, None)
    self.assertEqual(game._status, GameStatus.BATTLE)
    self.assertEqual(game._shuffle_strategy, self.shuffle_strategy)
    self.assertEqual(game._rank_score_strategy, self.ranking_strategy)
    self.assertEqual(game._winner, None)

  def test_game_prepare(self):
    game = Game(self.initial_deck, self.players, self.shuffle_strategy, self.ranking_strategy)

    player_1 = self.players[0]
    player_2 = self.players[1]

    self.assertEqual(player_1.isDeckEmpty(), True)
    self.assertEqual(player_2.isDeckEmpty(), True)

    game.prepare();

    self.assertEqual(player_1.isDeckEmpty(), False)
    self.assertEqual(player_2.isDeckEmpty(), False)

    player_one_cards = [player_1.popDeckTopCard(), player_1.popDeckTopCard()]
    player_two_cards = [player_2.popDeckTopCard(), player_2.popDeckTopCard()]

    isCardDifferent = True
    for card in player_one_cards:
      if card in player_two_cards:
        isCardDifferent = False
        break
    
    self.assertEqual(isCardDifferent, True)

  def test_game_setAndGetStatus(self):
    game = Game(self.initial_deck, self.players, self.shuffle_strategy, self.ranking_strategy)
    self.assertEqual(game.getStatus(), GameStatus.BATTLE)
    game._setStatus(GameStatus.WIN)
    self.assertEqual(game.getStatus(), GameStatus.WIN)

  def test_game_setAndGetWinner(self):
    game = Game(self.initial_deck, self.players, self.shuffle_strategy, self.ranking_strategy)
    self.assertEqual(game.getWinner(), None)
    
  def test_game_make_card_play(self):
    game = Game(self.initial_deck, self.players, self.shuffle_strategy, self.ranking_strategy)
    game.prepare()
    plays = game._makeCardPlays()

    #:: verify that each player's deck reduced by one. 
    player_1 = self.players[0]
    player_2 = self.players[1]

    self.assertEqual(player_1.getDeckSize(), 1)
    self.assertEqual(player_2.getDeckSize(), 1)
    self.assertEqual(len(plays), 2)
    
    #:: test sorting of plays from largest to smallest
    is_sorted_decreasing_order = True 
    for i in range(len(plays) - 1):
      card1 = plays[i][0]
      score1 = self.ranking_strategy.getScore(card1.getRank())
      card2 = plays[i + 1][0]
      score2 = self.ranking_strategy.getScore(card2.getRank())
      if score1 < score2: 
        is_sorted_decreasing_order = False 

    self.assertEqual(is_sorted_decreasing_order, True)