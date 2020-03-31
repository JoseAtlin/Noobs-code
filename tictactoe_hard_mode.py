import random

def move():
    A = [0,0,0,0,0,0,0,0,0]
    for i in range(1,10):
        if(board[i]=='X'):
            A[i-1] = 1
        elif(board[i]=='O'):
            A[i-1] = -1
    sums = [0,0,0,0,0,0,0,0]
    if(A[4] == 0):
        return 5
    else:
        sums[0] = A[0] + A[1] + A[2]
        sums[1] = A[3] + A[4] + A[5]
        sums[2] = A[6] + A[7] + A[8]
        sums[3] = A[0] + A[3] + A[6]
        sums[4] = A[1] + A[4] + A[7]
        sums[5] = A[2] + A[5] + A[8]
        sums[6] = A[0] + A[4] + A[8]
        sums[7] = A[2] + A[4] + A[6]
        i = sums.index(min(sums))
        if(sums[i]==-2):
            if i < 3:
                for j in range(3):
                    if A[(i*3)+j] == 0:
                        return (i*3) + j + 1
            elif i < 6:
                for j in range(3):
                    if A[(j*3) + i - 3] == 0:
                        return (j*3) + i - 2
            elif i == 6:
                for j in [0,4,8]:
                    if(A[j]==0):
                        return j+1
            else:
                for j in [2,4,6]:
                    if(A[j]==0):
                        return j+1
        i = sums.index(max(sums))
        if(sums[i]==2):
            if i  < 3:
                for j in range(3):
                    if A[(i*3)+j] == 0:
                        return (i*3) + j + 1
            elif i < 6:
                for j in range(3):
                    if A[(j*3) + i - 3] == 0:
                        return (j*3) + i - 2
            elif i == 6:
                for j in [0,4,8]:
                    if(A[j]==0):
                        return j+1
            else:
                for j in [2,4,6]:
                    if(A[j]==0):
                        return j+1
        else:
            for j in [0,2,6,8]:
                if(A[j]==0):
                    return j+1

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
		place = int(input("Enter a position to place \'X\' between 1 - 9 only : "))
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
	insLetter('O',move())
	

def isWinner(board,letter):
	if(board[1] == board[2] == board[3] == letter or board[4] == board[5] == board[6] == letter or board[7] == board[8] == board[9] == letter or board[1] == board[5] == board[9] == letter or	board[3] == board[5] == board[7] == letter or board[1] == board[4] == board[7] == letter or board[2] == board[5] == board[8] == letter or board[3] == board[6] == board[9] == letter):
		return True


pattern = [('.|.'*(2*i + 1)).center(140,'-') for i in range(5//2)]
print('\n'.join(pattern + ['WELCOME TO TIC TAC TOE'.center(140, '-')] + pattern[::-1]))

print("\n")
print(("Lets Play !!").center(140))
print("You are \'x\' and computer picks \'O\'".center(140))
print("\n")

while(1):
	flag = 0
	board = [' ']*10
	printBoard()
	while(board.count(' ') > 1):
		if not(isWinner(board,'O')):
			playerMove()
			printBoard()
		else:
			print("Sry,Better luck next time kid".center(140))
			flag = 1
			break

		if not(isWinner(board,'X')):
			compMove()
			printBoard()
		else:
			print("You won Mhhan !!".center(140))
			flag = 1
			break

	if flag == 0:
		if board.count(' ') == 1:
			print("Draw !!!")
	
	print("Do you wish to Restart the game?".center(140))
	print("Press 1.Restart 2.Exit".center(140))
	ch = int(input("Enter your choice : "))
	if ch == 2:
		break

