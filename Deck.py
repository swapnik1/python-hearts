from Card import Card
import random

class Deck:
	
	def __init__(self):
		self.cards = []
		for val in range(13):
			for suit in ["spade","heart","club","diamond"]:
				self.cards.append(Card(val+1,suit))

	def __repr__(self):
		out = str(len(self.cards)) + " cards in the deck.\n"
		for c in self.cards:
			out+=str(c)+"\n"
		return out

	def shuffle(self):
		random.shuffle(self.cards)

	def pop(self, c:Card=None):
		pop_i=0
		if c==None:
			return self.cards.pop(pop_i)
		found = False
		for i,v in enumerate(self.cards):
			if v==c:
				pop_i=i
				found=True
				break
		if not found:
			raise Exception("Card not in deck")
		return self.cards.pop(pop_i)