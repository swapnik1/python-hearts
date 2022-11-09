from Player import Player

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