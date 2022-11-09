

class Player:
	def __init__(self, name):
		self.name = name
		self.cards = []

	def __repr__(self):
		out = "Name : " + self.name + "\n"
		out += str(len(self.cards))+" Cards\n"
		out += "Cards : "
		for i,c in enumerate(self.cards):
			out += "("+i+") "+str(c)+" "
		return out