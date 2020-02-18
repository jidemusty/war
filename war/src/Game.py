from src.Player import Player 
from src.Deck import Deck 
from src.Card import Card, Rank, RankScore  

from typing import Iterable, Tuple, List 
from enum import Enum 

class GameStatus: 
  WAR = 'WAR'
  WIN = 'WIN'
  BATTLE = 'BATTLE' 

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
    deck = self._playing_deck.clone() 
    self._shuffle_strategy.shuffleDeck(deck)
    #:: split evenly among players. 
    num_players = len(self._players) 
    next_player = 0 
    expected_count = (deck.size() // num_players) * num_players 
    count = 0 

    while (~deck.isEmpty() and count < expected_count):
      card = deck.popTopCard() 
      self._players[next_player].addToDeckBottom([card]) 
      next_player = (next_player + 1) % num_players
      count += 1

  def getStatus(self) -> GameStatus: 
    return self._status 

  def _checkForWinner(self):
    """ set game status to 'WIN' if there's a winner. 
    """
    num_players_with_card = 0
    winner = None 
    for player in self._players:
      if ~player.isDeckEmpty():
        num_players_with_card += 1
        winner = player 

    #:: if we have only one player with a non-empty deck...that is the winner.
    if (num_players_with_card == 1):
     self._setStatus(GameStatus.WIN)
     self._winner = winner # 

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

      plays.append((card,player))
    #::sort the plays in decreasing order. 
    #::for the key, use the first item which is the card. 
    sort_key = lambda item: self._rank_score_strategy.getScore(item[0].getRank())
    plays.sort(key = sort_key, reversed=True)

    return plays 

  def _setStatus(self, status: GameStatus):
    self._status = status 

  def _makeBattlePlay(self):
    #:: check if we have a winner. 
    self._checkForWinner()
    if (self.getStatus() == GameStatus.WIN): 
      # we have a winner. 
      return 
    # make a play. 
    plays = self._makeCardPlays()
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

  def _makeWarPlay(self):
    """ makes the war game play """
    self._checkForWinner()
    if (self.getStatus() == GameStatus.WIN):
      return 

    #: make plays from players. (first cards down)
    plays = self._makeCardPlays() 
    #:: make the second plays from players. (similar to battle play)
    self._makeBattlePlay()


  def makePlay(self):
    """ executes one round of play for war game """
    status = self.getStatus() 
    if status == GameStatus.WAR:
      self._makeWarPlay()
    elif status == GameStatus.BATTLE:
      self._makeBattlePlay() 
    else: 
      # means we have a winner. 
      print("Winner: ", self.getWinner())


  def start(self):
    #:: starts the game loop 
    while (self.getStatus() != GameStatus.WIN):
      self.makePlay() 
      input("Enter to make next game play")
    #:: at this point game has ended. 
    
    
    



  