
class Trick:
	def __init__(self, players:list, start_i:int):
		self.players = players
		self.start_i=start_i
		self.suit=""
		self.trickCards = []

	def __repr__(self):
		out=""
		if len(self.trickCards)==0:
			return "First play\n"
		out+="Suit : "+self.suit+"\n"
		out+="Cards played : "+str(self.trickCards)+"\n"
		return out


	def play(self):
		s=0
		n=len(self.players)
		while s<n:
			p = self.players[(self.start_i+s)%n]
			print(self)
			c = p.selectCardToPlay(self.suit)
			p.playCard(c)
			self.trickCards.append(c)
			if not self.suit:
				self.suit=c.suit
			s+=1

		print(self)
		return self.getWinner()

	def getWinner(self):
		highCard = 0
		highPlayer = 0
		for i,c in enumerate(self.trickCards):
			if (c.suit==self.suit) and (c.value>highCard):
				highCard=c.value
				highPlayer=i
		# Winner is the player who went ith
		return (self.start_i+highPlayer)%len(self.players)

	def points(self):
		points = 0
		for c in self.trickCards:
			if c.suit == 'heart':
				points += 1
			if (c.value == 12) and (c.suit == 'spade'):
				points += 13
		return points



