"""
Tic tac toe

By: Gabriel Avendaño 
"""

#important functions

# gets the x y from user
def input_move ():
	while True: 
		try:
			inp = list(map(int, input("Where do you want to play? ").split()))
			if len(inp) == 2:
				if (1 <= inp[0] <= 3) and (1 <= inp[1] <= 3):
					break
				else:
					print("remember it is from 1 to 3")
			else :
				print ("I only need two numbers for (x  y), between 1 and 3")
		except:
			print("I dont understand, remember it is (x  y) from 1 to 3") 
	return [inp[0]-1, inp[1]-1]

def check_win(l_game, l_players, l_symbols):
	# check rows
	for row in l_game:
		if row[0] in l_symbols and row[0] == row [1] and row[1] == row[2]:
			return l_players[l_symbols.index(row[0])]

	# check columns
	for column in range (len(l_game)):
		if l_game[0][column] in l_symbols and l_game[0][column] == l_game[1][column] and l_game[1][column] == l_game[2][column]:
			return l_players[l_symbols.index(l_game[0][column])]

	return ""

def print_game(l_game):
	for y in range(2, -1, -1):
		print(l_game[y][0] + "\t" + l_game[y][1] + "\t" + l_game[y][2])

# introduction
print ("hello, This is a simple tic tac toe game ")
print ("The input will be in the form of a grid")
print ("Each player will choose a position in a (x, y) coordinates")

# user choosing symbol # or X
s_player1_simbol = ""
s_player2_simbol = ""
while not(s_player1_simbol == "#" or s_player1_simbol == "X"):
	s_player1_simbol = input("first player choose between # or X : ")
	s_player1_simbol = s_player1_simbol.upper()

if s_player1_simbol == "X":
	s_player2_simbol = "#"
else:
	s_player2_simbol = "X"


# game begins
print ("\nLets begin the game\n")


l_players = ["player 1", "player 2"]
l_symbols = [s_player1_simbol, s_player2_simbol]
i_turn = 0

l_game = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
s_winner = ""
b_endgame = False

while not b_endgame:
	print (l_players[i_turn] + " turn")
	l_move = input_move()
	while l_game[l_move[1]][l_move[0]] != "_":
		print ("that place is already taken, sorry. Please move again")
		l_move = input_move()

	l_game[l_move[1]][l_move[0]] = l_symbols[i_turn]
	
	print_game(l_game)

	s_winner = check_win(l_game, l_players, l_symbols)
	if s_winner is not "":
		b_endgame = True

	i_turn = (i_turn + 1) % 2 


print ("The winner is " + s_winner)