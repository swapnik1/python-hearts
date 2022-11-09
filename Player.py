from Card import Card

class Player:
	def __init__(self, name):
		self.name = name
		self.cards = []

	def __repr__(self):
		out = "Name : " + self.name + "\n"
		out += str(len(self.cards))+" Cards\n"
		out += "Cards :\n"
		for i,c in enumerate(self.cards):
			out += str(c)+". "
			if i%7==6:
				out += "\n"

		return out

	def addCard(self, c:Card):
		self.cards.append(c)

	def sortCards(self):
		self.cards.sort(key=lambda x: (x.suit, x.value))