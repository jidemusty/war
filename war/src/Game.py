from enum import Enum 
from src.Deck import Deck 
from src.Player import Player 
from typing import Iterable, Tuple, List
from src.Card import Card, Rank, RankScore  
from src.Shuffle import DeckShuffleStrategy

class GameStatus: 
  WAR = 'WAR'
  WIN = 'WIN'
  BATTLE = 'BATTLE' 
  DRAW = 'DRAW'

class Game: 
  def __init__(self, playing_deck: Deck, players: Iterable[Player], shuffle_strategy: DeckShuffleStrategy, rank_score_strategy: RankScore):
    self._players = players #:: deck must be even in length / divisible by the number of players. 
    #:: this represents the card deck for the game. 
    self._playing_deck = playing_deck
    self._current_play_deck = None 
    self._status = GameStatus.BATTLE
    self._shuffle_strategy = shuffle_strategy 
    self._rank_score_strategy = rank_score_strategy 
    self._winner = None 

  def prepare(self): 
    """ Prepares the Deck of Cards, and splits it evenly among players """
    #:: shuffle the playing deck. 
    #:: copy
    self._current_play_deck = Deck()
    cards = self._playing_deck.getCards()
    deck = Deck()
    deck.extend(cards)
    self._shuffle_strategy.shuffleDeck(deck)
    #:: split evenly among players. 
    num_players = len(self._players) 
    next_player = 0 
    expected_count = (deck.size() // num_players) * num_players 
    count = 0 

    while (not deck.isEmpty() and count < expected_count):
      card = deck.popTopCard() 
      self._players[next_player].addToDeckBottom([card]) 
      next_player = (next_player + 1) % num_players
      count += 1

  def getStatus(self) -> GameStatus: 
    return self._status 

  def _checkForDrawOrWinner(self):
    """ set game status to 'WIN' if there's a winner. 
    """
    num_players_with_card = 0
    winner = None 
    for player in self._players:
      if not player.isDeckEmpty():
        num_players_with_card += 1
        winner = player 

    #:: if we have only one player with a non-empty deck...that is the winner.
    if (num_players_with_card == 1):
     self._setStatus(GameStatus.WIN)
     self._winner = winner
    elif (num_players_with_card == 0):
      self._setStatus(GameStatus.DRAW)
      self._winner = None 

  def getWinner(self):
    """ returns the game winner. This is the player with a non-empty deck """ 
    return self._winner 

  def _makeCardPlays(self) -> List[Tuple[Card, Player]]:
    """ gets all the top cards from the players, and adds it to current deck """
    plays = []
    for player in self._players: 
      card = player.popDeckTopCard()
      #: add the card to the current playing deck. 
      self._current_play_deck.pushToTop(card) 

      plays.append((card, player))
    #::sort the plays in decreasing order. 
    #::for the key, use the first item which is the card. 
    sort_key = lambda item: self._rank_score_strategy.getScore(item[0].getRank())
    plays.sort(key = sort_key, reverse=True)

    return plays 

  def printPlayerDecks(self):
    print("Player Decks   ####################################")
    for player in self._players:
      player.printDeck()
    print("###################################################")
    
  def _setStatus(self, status: GameStatus):
    self._status = status 

  def _makeBattlePlay(self):
    #:: print current decks of players 
    self.printPlayerDecks()
    #:: check if we have a winner. 
    self._checkForDrawOrWinner()
    if (self.getStatus() == GameStatus.WIN or self.getStatus() == GameStatus.DRAW): 
      # we have a winner. 
      return 
    # make a play. 
    plays = self._makeCardPlays()
    self.printPlays(plays)
    #:: the player who wins this round is at the top of plays. 
    #:: if both cards are of the same rank...then it's war. 
    if self._rank_score_strategy.getScore(plays[0][0].getRank()) == self._rank_score_strategy.getScore(plays[1][0].getRank()):
      #:: this means war. 
      self._setStatus(GameStatus.WAR)
    else:
      #:: give the current deck to the highest card. 
      self._setStatus(GameStatus.BATTLE) 
      winning_player = plays[0][1] 
      winning_player.addToDeckBottom(self._current_play_deck.popAll())
      print("Game: Assigneed Deck to ", winning_player.getName())

  def printPlays(self, plays):
    print("The current card played ")
    for i in range(len(plays)):
      player = plays[i][1]
      print("[{}] ".format(player.getName()), str(plays[i][0]))
    print("##########################")
    
  def _makeWarPlay(self):
    """ makes the war game play """
    self.printPlayerDecks()
    self._checkForDrawOrWinner()
    
    if (self.getStatus() == GameStatus.WIN or self.getStatus() == GameStatus.DRAW): 
      # we have a winner. 
      return 

    #: make plays from players. (first cards down)
    plays = self._makeCardPlays()
    self.printPlays(plays)
    #:: make the second plays from players. (similar to battle play)
    self._makeBattlePlay()

  def makePlay(self):
    """ executes one round of play for war game """
    status = self.getStatus() 
    #:: print player card
    if status == GameStatus.WAR:
      self._makeWarPlay()
    elif status == GameStatus.BATTLE:
      self._makeBattlePlay() 
      # means we have a winner.
    print("Game Status: ", self.getStatus())

  def start(self):
    #:: starts the game loop
    self.prepare()
    while (self.getStatus() != GameStatus.WIN and self.getStatus() != GameStatus.DRAW):
      self.makePlay()
      input("Press Enter key to make next game play ")

    if self.getStatus() == GameStatus.WIN:
      print("Winner: ", self._winner.getName())
    else:
      print("Draw")
    #:: at this point game has ended. 
  