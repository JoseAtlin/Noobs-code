import numpy as np

def printGrid():
	print(' '.join(str(row_matrix[0])).replace('[','').replace(']','').center(140))
	print(' '.join(str(row_matrix[1])).replace('[','').replace(']','').center(140))
	print(' '.join(str(row_matrix[2])).replace('[','').replace(']','').center(140))
	print(('-'*35).center(140))
	print(' '.join(str(row_matrix[3])).replace('[','').replace(']','').center(140))
	print(' '.join(str(row_matrix[4])).replace('[','').replace(']','').center(140))
	print(' '.join(str(row_matrix[5])).replace('[','').replace(']','').center(140))
	print(('-'*35).center(140))
	print(' '.join(str(row_matrix[6])).replace('[','').replace(']','').center(140))
	print(' '.join(str(row_matrix[7])).replace('[','').replace(']','').center(140))
	print(' '.join(str(row_matrix[8])).replace('[','').replace(']','').center(140))

def checkRow(pos):
	not_possible[pos] = list(set(np.append(not_possible[pos],row_matrix[pos//9]).astype(int))) 

def checkColumn(pos):
	not_possible[pos] = list(set(np.append(not_possible[pos],column_matrix[pos%9]).astype(int)))

def checkBox(pos):
	l=[]
	r_st,c_st = (((pos//9)//3)*3),(((pos%9)//3)*3)
	for i in range(r_st,r_st+3):
		for j in range(c_st,c_st+3):
			l.append(row_matrix[i][j])
	not_possible[pos] = list(set(np.append(not_possible[pos],l).astype(int)))

def checkNot(pos,insert):					#these functions keep track of the not_possible numbers for a given space
	temp = (pos//9)*9					#By checking row, column, and the nonet, since they are unique
	for i in range(temp,temp+9):				#Initially those 81 lists will be set from the puzzle provided
		if insert not in not_possible[i]:		#whenever the algorithm finds the correct value of a spot, it will append the
			not_possible[i].append(insert)		#the value to row_matrix,column_matrix and the the lists that are related to
	temp = pos % 9						#that position, i.e. 21 spots -> 9 row_elements + 9 column_elements + 9 
	for i in range(temp,temp+73,9):				#nonet elements. Snce there would be 5 repetitions. 
		if insert not in not_possible[i]:
			not_possible[i].append(insert)
	start = (((pos//9)//3)*27) + (((pos%9)//3)*3)
	for i in range(start,start+27,9):
		for j in range(i,i+3):
			if insert not in not_possible[j]:
				not_possible[j].append(insert)
	


f = open('puzzle.txt',mode='r')				#collecting the puzzle from a file
array = []						#blanks should be inserted as 0's and the numbers in grid should be from (1 - 9)
for line in f:						
	for num in line:
		if num.isdigit():
			array.append(int(num))

array = np.array(array)					#Matrix to store the row-wise numbers and column-wise numers separately
row_matrix = array.reshape(9,9)				
column_matrix = row_matrix.T
not_possible = [[]]*81					#creating 81 lists, as there are 81 spots in a Sudoku

print('\n')
print("The given Sudoku Grid :\n".center(140))
printGrid()

i = 0
while i < 81 :
	checkRow(i)
	checkColumn(i)
	checkBox(i)
	i += 1

while(1):						#looping until the matrix has no 0's i.e. blanks left
	pos = 0
	while(pos < 81):
		if len(not_possible[pos]) == 9 and row_matrix[pos//9][pos%9] == 0:
			for check in range(10):
				if check not in not_possible[pos]:
					row_matrix[pos//9][pos%9] = check	#updating te row_matrix and column_matrix
					column_matrix[pos%9][pos//9] = check	#updating all the lists associated with this position
					checkNot(pos,check)			#	*21 lists*
					#print(pos,not_possible[pos])
					#print(row_matrix)
					break
			break
		pos += 1
	if 0 not in row_matrix:	
		break

print('\n')
print("Solved Sudoku : \n".center(140))
printGrid()

