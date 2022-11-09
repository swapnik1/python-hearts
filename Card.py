
class Card:
	def __init__(self, value, suit):
		if value not in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
			raise ValueError("Invalid value for the card")

		if not suit.isalpha():
			raise ValueError("Invalid suit for the card")
		suit = suit.lower()
		if suit not in ["spade","heart","club","diamond"]:
			raise ValueError("Invalid suit type for the card")

		self.value = value
		self.suit = suit

	def __repr__(self):
		return self.getValue()+" of "+self.suit+"s"

	def getValue(self):
		valMap = {
			1:"A",
			2:"2",
			3:"3",
			4:"4",
			5:"5",
			6:"6",
			7:"7",
			8:"8",
			9:"9",
			10:"10",
			11:"J",
			12:"Q",
			13:"K"
		}
		return valMap[self.value]

	def __eq__(self,other):
		if other==None:
			return False
		if (self.value == other.value) and (self.suit == other.suit):
			return True
		return False