import random
def display_board() :
	print("*************************")
	print("*\t O | X | X \t*")
	print("*\t---|---|---\t*")
	print("*\t X | O | X \t*")
	print("*\t---|---|---\t*")
	print("*\t O | X | O \t*")
	print("*************************")

def playe():
	players=["O","X"]
	player=random.choices(players)
	return player[0]
print(playe())
def player_input(player):
	row=int(input("row : "))
	column=int(input("column : "))
	return row,column
print(player_input(player))
def play():
	li_O=[]
	li_X=[]
	jouer=playe()
	if player[0]=="O":
		print(f"Player {player}'s turn ... ")
		mise=player_input(player)
	cart=display_board()

print(play())