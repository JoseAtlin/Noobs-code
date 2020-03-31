import numpy.random as np

def printBoard():
	print((board[1] + '|' + board[2] + '|' + board[3]).center(140))
	print((board[4] + '|' + board[5] + '|' + board[6]).center(140))
	print((board[7] + '|' + board[8] + '|' + board[9]).center(140))

def insLetter(letter,pos):
	board[pos] = letter

def free(pos):
	if board[pos] == ' ':
		return True

def playerMove():
	while(1):
		place = int(raw_input("Enter a position to place \'X\' between 1 - 9 only : "))
		if place < 10 and place > 0:
			if free(place):	
				insLetter('X',place)
				break
			else:
				print(("The position is already occupied").center(140,'-'))
		elif place > 9 or place < 1:
			print(("Invalid position").center(140,'-'))

def compMove():
	print("Computer is making the Move :")
	l = []
	for i in range(1,10):
		if board[i] == ' ':
			l.append(i)
	insLetter('O',np.choice(l))
	

def isWinner(board,letter):
	if(board[1] == board[2] == board[3] == letter or board[4] == board[5] == board[6] == letter or board[7] == board[8] == board[9] == letter or board[1] == board[5] == board[9] == letter or	board[3] == board[5] == board[7] == letter or board[1] == board[4] == board[7] == letter or board[2] == board[5] == board[8] == letter or board[3] == board[6] == board[9] == letter):
		return True


pattern = [('.|.'*(2*i + 1)).center(140,'-') for i in range(5//2)]
print('\n'.join(pattern + ['WELCOME TO TIC TAC TOE'.center(140, '-')] + pattern[::-1]))

print("\n\n")
print(("Lets Play !!").center(140))
print("You are \'x\' and computer picks \'O\'\n".center(140))
print("\n\n")
board = [' ']*10
printBoard()

while(board.count(' ') > 1):
	if not(isWinner(board,'O')):
		playerMove()
		printBoard()
	else:
		print("Better luck next time kid ;)")
		break
	
	if not(isWinner(board,'X')):
		compMove()
		printBoard()
	else:
		print("You won Mhhan !!")
		break

if board.count(' ') == 1:
	print("Draw !!!")

