from src.Deck import Deck
from src.Card import Card, Rank, Suite
from typing import List 

def createPlayingDeck(suites: List[Suite], ranks: List[Rank]) -> Deck:
  deck = Deck() 
  for rank in ranks:
    for suite in suites:
      card = Card(rank, suite)
      deck.pushToTop(card) 

  return deck 