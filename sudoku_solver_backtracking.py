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

def isEmpty(matrix,l): 
	for i in range(9): 
		for j in range(9): 
			if(matrix[i][j] == 0): 
				l[0] = i 
				l[1] = j 
				return True
	return False

def usedRow(matrix,row,check): 
    for i in range(9): 
        if(matrix[row][i] == check): 
            return True
    return False
  
def usedCol(matrix,col,check): 
    for i in range(9): 
        if(matrix[i][col] == check): 
            return True
    return False
  
def usedBox(matrix,row,col,check): 
    for i in range(3): 
        for j in range(3): 
            if(matrix[i+row][j+col] == check): 
                return True
    return False
  
def isSafe(matrix,row,col,num): 
    return not usedRow(matrix,row,num) and not usedCol(matrix,col,num) and not usedBox(matrix,row - row%3,col - col%3,num) 
  
 
def solve(arr): 
	l=[0,0] 
	if(not isEmpty(arr,l)): 
		return True

	row = l[0] 
	col = l[1]
	for put in range(1,10):
		if(isSafe(matrix,row,col,put)): 
			matrix[row][col] = put 
			if(solve(matrix)): 
				return True
		matrix[row][col] = 0

	return False 

f = open('puzzle3.txt',mode='r')				
array = []						
for line in f:						
	for num in line:
		if num.isdigit():
			array.append(int(num))

array = np.array(array)					
matrix = array.reshape(9,9)
print('\n')
print("The given Sudoku Grid :\n".center(140))
printGrid()
if solve(matrix):
	print("\n")
	print("Solved Sudoku :".center(140))
	printGrid()
else:
	print("Not Possible or check the inputs")
