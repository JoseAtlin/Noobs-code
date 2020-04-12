import numpy as np

def printGrid():
	print(' '.join(str(matrix[0])).replace('[','').replace(']','').center(140))
	print(' '.join(str(matrix[1])).replace('[','').replace(']','').center(140))
	print(' '.join(str(matrix[2])).replace('[','').replace(']','').center(140))
	print(('-'*35).center(140))
	print(' '.join(str(matrix[3])).replace('[','').replace(']','').center(140))
	print(' '.join(str(matrix[4])).replace('[','').replace(']','').center(140))
	print(' '.join(str(matrix[5])).replace('[','').replace(']','').center(140))
	print(('-'*35).center(140))
	print(' '.join(str(matrix[6])).replace('[','').replace(']','').center(140))
	print(' '.join(str(matrix[7])).replace('[','').replace(']','').center(140))
	print(' '.join(str(matrix[8])).replace('[','').replace(']','').center(140))

def isEmpty(l): 				#to check the spots where we need to fill numbers
	for i in range(9): 
		for j in range(9): 
			if(matrix[i][j] == 0): 
				l[0] = i 
				l[1] = j 
				return True
	return False

def usedRow(row,check): 			#to check if the number is anywhere in the row
    for i in range(9): 
        if(matrix[row][i] == check): 
            return True
    return False
  
def usedCol(col,check): 			#to check if the number is anywhere in the column
    for i in range(9): 
        if(matrix[i][col] == check): 
            return True
    return False
  
def usedBox(row,col,check): 			#to check if the number if anywhere in the box
    row -= row % 3	
    col -= col % 3
    for i in range(3): 
        for j in range(3): 
            if(matrix[i+row][j+col] == check): 
                return True
    return False
  
def isSafe(row,col,num): 			#checks if the element to insert is not in any of the column, row, box
    return not usedRow(row,num) and not usedCol(col,num) and not usedBox(row,col,num) 
  
 
def solve(): 
	l=[0]*2					#keep track of the row and colums of sudoku matrix
	if(not isEmpty(l)): 
		return True			#if there is not empty spots left, which means solution found

	row = l[0] 
	col = l[1]
	for put in range(1,10):			#chooses a number from 1 - 9
		if(isSafe(row,col,put)): 
			matrix[row][col] = put 	#puts the number that is not present in row, column, box
			if(solve()): 	
				return True	#moves to the next spot
		matrix[row][col] = 0

	return False 				#returns if there is no possibility to solve the puzzle

f = open('puzzle3.txt',mode='r')		#reading the input puzzle from the ".txt" file
array = []					
for line in f:						
	for num in line:
		if num.isdigit():
			array.append(int(num))	

array = np.array(array)				#reshaped to matrix to access the elements in sudoku format	
matrix = array.reshape(9,9)
print('\n')
print("The given Sudoku Grid :\n".center(140))
printGrid()
if solve():
	print("\n")
	print("Solved Sudoku :".center(140))
	printGrid()
else:
	print("Not Possible or check the inputs")
