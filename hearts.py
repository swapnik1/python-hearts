from Player import Player
from Deck import Deck

def distributeCards(deck, players):
	i=0
	n = len(players)
	# if 5 players, remove spade and diamond 2s from the deck
	if n==5:
		deck.pop(Card(2,"spade"))
		deck.pop(Card(2,"diamond"))
	while len(deck.cards)!=0:
		i=i%n
		player = players[i]
		player.addCard(deck.pop())
		i+=1
	for p in players:
		p.sortCards()

# Pick total number of players(4 or 5)
# n = int(input("Total number of players? (4-5)"))
n=4

players = []
for i in range(n):
	# name = input("Enter player "+str(i)+" name:")
	name=""
	if not name:
		name = "Player "+str(i+1)
	players.append(Player(name))

# Get a deck of cards
deck = Deck()

# Shuffle cards
deck.shuffle()

# distribute all cards
distributeCards(deck, players)
