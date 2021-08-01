import math

board = [
		[0,3,0,0,0,0,0,0,0],
		[0,2,0,9,0,6,3,0,0],
		[0,6,0,4,0,2,0,9,0],
		[1,0,0,0,9,0,4,0,0],
		[0,0,8,1,0,3,5,0,0],
		[0,0,5,0,7,0,0,0,3],
		[0,5,0,3,0,1,0,6,0],
		[0,0,4,6,0,7,0,3,0],
		[0,0,0,0,0,0,0,8,0]
		]

def ROW_CHECK(num,row) :

	for i in board[row] :
		if i == num :
			return False
	else :
		return True

def COL_CHECK(num,col) :

	for i in range(0,9):
		if board[i][col] == num :
			return False
	else :
		return True

def BLK_CHECK(num,row,col) :

	for i in range((3*math.floor(row/3)),(3*math.floor(row/3)) + 3) :
		for j in range((3*math.floor(col/3)),(3*math.floor(col/3)) + 3) :
			if board[i][j] == num :
				return False
	else :
		return True

def EMPTY() :

	for i in range(0,9) :
		for j in range(0,9) :
			if board[i][j] == 0 :
				return True
	return False

def LOC() :

	for i in range(0,9) :
		for j in range(0,9) :
			if board[i][j] == 0 :
				l = [i,j]
				return l

def VALID(num,row,col) :

	if ROW_CHECK(num,row) and COL_CHECK(num,col) and BLK_CHECK(num,row,col) :
		return True
	else :
		return False

def SOLVE() :

	if not EMPTY() :
		return True
	l = LOC()
	for n in range(1,10) :
		if VALID(n,l[0],l[1]) :
			board[l[0]][l[1]] = n
			if SOLVE() :
				return True
			board[l[0]][l[1]] = 0
	return False

SOLVE()

print()
for i in range(0,9) :
	print(board[i])