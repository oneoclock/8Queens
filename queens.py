import json
f=open("place.json","r")
board=json.loads(f.read())
board=board["matrix"]

def issafe(row,col):
	for i in range(8):
		for j in range(8):
			if board[i][j]==1:
				if row==i:
					return False
				if col==j:
					return False
				if abs(row-i)==abs(col-j):
					return False
	return True
def place(col):
	if(col>=8):
		return True
	for i in range(8):
		if issafe(i,col):
			board[i][col]=1
			
			if place(col+1):
				return True
		board[i][col]=0
	return False
if place(1)==True:
	for i in range(8):
		print board[i]
else: 
	print False
