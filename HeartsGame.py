from Deck import Deck
from Card import Card
from Trick import Trick

class HeartsGame:
	def __init__(self, players:list):
		self.players = players
		self.n = len(players)
		self.scores = [0]*self.n
		self.passing = [1,-1,2,0]
		if self.n == 5:
			self.passing = [1,-1,2,-2,0]
		self.pass_n = len(self.passing)

	def play(self):
		self.round_i = 0
		while max(self.scores)<100:
			# Start round
			roundScores = [0]*self.n

			# distribute all cards
			self.distributeCards()

			# Passing around
			pass_direction = self.passing[self.round_i%self.pass_n]
			self.passCards(pass_direction)

			# find player with 2 of clubs
			p_i = self.findPlayerWithCard(Card(2,'club'))

			start_pl = p_i
			trick_i=0
			# While players are not out of cards
			while len(self.players[0].cards)>0:
				# Start trick with 2 of clubs or winner of last trick
				trick = Trick(self.players, start_pl)

				# players play cards, one player wins trick
				start_pl = trick.play()

				t_points = trick.points()

				# Winner takes all the points of the trick
				roundScores[start_pl] += t_points

				# End trick
				print(self.players[start_pl].name+" got "+str(t_points)+" points\n")

			# All cards played, End Round, Check for shoot the moon
			shoot_moon_player = -1
			if max(roundScores)==26:
				for i,v in enumerate(roundScores):
					if roundScores[i]==0:
						roundScores[i]=26
					else:
						shoot_moon_player = i
						roundScores[i]=0

			# Update scores
			for i,v in enumerate(roundScores):
				self.scores[i]+=v

			# Print status
			print("Round #"+str(self.round_i)+"\n")
			if shoot_moon_player!=-1:
				print(self.players[p_i].name+" shot the moon!!")
			for p_i,score in enumerate(roundScores):
				print(self.players[p_i].name+" score: "+str(score)+"\n")
			self.round_i+=1

	def passCards(self, pass_direction):
		if pass_direction == 0:
			return

		direction="right"
		if pass_direction <0:
			direction="left"

		print("Passing cards "+str(abs(pass_direction))+ " to the "+direction+"\n")

		target = [None]*self.n
		# For each player, select cards to pass
		for i,p in enumerate(self.players):
			cardsToPass = p.getCardsToPass()
			t = (i+pass_direction)%self.n
			target[t]=cardsToPass

			for c in cardsToPass:
				p.playCard(c)

		# add cards to receiving players hand
		for t,cards in enumerate(target):
			self.players[t].addCards(cards)


	def distributeCards(self):
		# Get a deck of cards
		deck = Deck()

		# Shuffle cards
		deck.shuffle()

		i=0
		n = len(self.players)
		# if 5 players, remove spade and diamond 2s from the deck
		if n==5:
			deck.pop(Card(2,"spade"))
			deck.pop(Card(2,"diamond"))
		while len(deck.cards)!=0:
			i=i%n
			player = self.players[i]
			player.addCard(deck.pop())
			i+=1
		for p in self.players:
			p.sortCards()

	def findPlayerWithCard(self, card:Card):
		for i,p in enumerate(self.players):
			if p.hasCard(card):
				return i
		return -1