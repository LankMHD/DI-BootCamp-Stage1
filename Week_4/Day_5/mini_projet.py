inter=[
	[" "," "," "],
	[" "," "," "],
	[" "," "," "]
	]

def display_board(inter):
	print("\nTIC TAC TOE")
	print(f"***************")
	print(f"*  {inter[0][0]} | {inter[0][1]} | {inter[0][2]}  *")
	print(f"* ---|---|--- *")
	print(f"*  {inter[1][0]} | {inter[1][1]} | {inter[1][2]}  *")
	print(f"* ---|---|--- *")
	print(f"*  {inter[2][0]} | {inter[2][1]} | {inter[2][2]}  *")
	print(f"***************")


def player_input():

	cmpt=1
	while cmpt<=9:
		if cmpt%2!=0:
			player="X"
			print("\nPlayer X's turn ... \n")
			row=int(input("Enter row : "))
			row=row-1
			while row<0 and row>3:
				print("Enter a number between 0 and 3")
				row=int(input("Enter row : "))
				row=row-1
			column=int(input("Enter column : "))
			column=column-1
			while column<0 and column>3:
				print("Enter a number between 0 and 3")
				column=int(input("Enter column : "))
				column=column-1
			while inter[row][column].isalpha():
				print("Case yet occupied ! \n")
				row=int(input("Enter row : "))
				row=row-1
				column=int(input("Enter column : "))
				column=column-1
			else:
				inter[row][column]=player
			display_board(inter)
			chek_win()

		else:
			player="O"
			print("\nPlayer O's turn ... \n")
			row=int(input("Enter row : "))
			row=row-1

			column=int(input("Enter column : "))
			column=column-1

			while inter[row][column].isalpha():
				print("Case yet occupied ! \n")
				row=int(input("Enter row : "))
				row=row-1
				column=int(input("Enter column : "))
				column=column-1
			else:
				inter[row][column]=player
			display_board(inter)
			chek_win()
		cmpt+=1
	print("MATCH NULL !!! \n\n GAME OVER !! \n\n Good Bye!!!!!!")
	
	


def chek_win():
	player_X=[]
	for r_c in inter:
		i=0
		while r_c!=[] and i<3:
			if r_c[i]=="X":
				player_X.append(i)
			i+=1

	player_O=[]
	for r_c in inter:
		i=0
		while r_c!=[] and i<3:
			if r_c[i]=="O":
				player_O.append(i)
			i+=1

	win=[
			[0,0,0],
			[1,1,1],
			[2,2,2],
			[0,1,2],
			[2,1,0]
		]

	if player_O in win:
		print("Player O is the winner !!! ")
		print("\n\t Game over !!\n\n Good bye!!!!")
		exit()
	elif player_X in win:
		print("Player X is the winner !!! ")
		print("\n\t Game over !!\n\n Good bye!!!!")
		exit()





def play():
	print("\n                         _____________")
	print("*********************** | TIC TAC TOE | ******************************")
	print("                        |_____________|")
	display_board(inter)
	player_input()
play()