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
			out += str(i)+") "+str(c)+". "
			if i%7==6:
				out += "\n"

		return out

	def addCard(self, c:Card):
		self.cards.append(c)

	def addCards(self, cards:list):
		self.cards+=cards
		self.sortCards()

	def sortCards(self):
		self.cards.sort(key=lambda x: (x.suit, x.getValue()))

	def selectCardToPlay(self, trick_suit):
		print(self)
		i = int(input("Select card to play :"))
		return self.cards[i]

	def playCard(self, c:Card):
		found=False
		c_i=0
		for i,x in enumerate(self.cards):
			if x==c:
				found=True
				c_i=i
		if found:
			return self.cards.pop(c_i)
		raise Exception("Player doesn't have the card : "+str(c))

	def hasCard(self, x:Card):
		for c in self.cards:
			if x==c:
				return True
		return False

	def getCardsToPass(self):
		print(self)
		to_pass = input("Select cards to pass :(For example : 1,2,3)")
		to_pass = to_pass.split(",")
		return [
			self.cards[int(to_pass[0])],
			self.cards[int(to_pass[1])],
			self.cards[int(to_pass[2])]
		]