import pygame
import time

board = [
		['|',' ','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|'],
		['|',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
		['|',' ','|',' ','|','|','|',' ','|',' ','|','|','|','|','|','|','|','|','|'],
		['|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
		['|',' ','|','|','|',' ','|','|','|','|','|','|','|','|','|','|',' ','|','|'],
		['|',' ','|',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ','|',' ','|','|'],
		['|',' ','|','|','|','|','|',' ','|','|','|','|','|',' ','|','|',' ',' ','|'],
		['|',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ','|',' ','|',' ',' ',' ','|'],
		['|','|','|',' ','|',' ','|','|','|','|','|',' ','|',' ','|',' ','|',' ','|'],
		['|',' ',' ',' ','|',' ','|',' ',' ',' ','|',' ','|',' ','|',' ','|',' ','|'],
		['|','|','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|'],
		['|',' ',' ',' ','|',' ',' ',' ','|',' ','|',' ','|',' ',' ',' ','|',' ','|'],
		['|',' ','|','|','|','|','|','|','|',' ','|','|','|','|','|','|','|','|','|'],
		['|',' ',' ',' ',' ',' ',' ',' ','|',' ','|',' ',' ',' ',' ',' ',' ',' ','|'],
		['|','|','|','|','|',' ','|',' ','|',' ','|',' ','|','|','|','|','|',' ','|'],
		['|',' ',' ',' ','|',' ','|',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ','|'],
		['|',' ','|','|','|',' ','|',' ','|','|','|','|','|',' ','|',' ','|',' ','|'],
		['|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ','|',' ','|',' ',' '],
		['|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|']
		]

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SD = pygame.display.set_mode((608,608))

start = (0,1)
end = (17,18)

def BLOCKS(board) :

	for i in range(0,len(board)) :
		for j in range(0,len(board)) :
			if board[i][j] == '|' :
				pygame.draw.rect(SD,BLUE,(j * 32,i * 32,32,32))
			pygame.draw.rect(SD,RED,(start[1] * 32,start[0] * 32,32,32))
			pygame.draw.rect(SD,RED,(end[1] * 32,end[0] * 32,32,32))

def DISTANCE(initial,final) :

	return abs((initial[0] - final[0]) + (initial[1] - final[1]))

def ASTAR(start,end) :

	if start == end :
		return None , []
	openlist = [start]
	nodes = {start:['',0]} # node:[parent,value]
	closedlist = []
	while openlist :
		currentnode = openlist[0]
		for node in openlist[1:] :
			if nodes[node][1] + DISTANCE(node,end) < nodes[currentnode][1] + DISTANCE(node,end) :
				currentnode = node
		if currentnode == end :
			break
		openlist.remove(currentnode)
		closedlist.append(currentnode)
		for a,b in [(0,1),(0,-1),(1,0),(-1,0)] : # (1,1),(1,-1),(-1,1),(-1,-1) to allow diagonal
			x = currentnode[0] + a
			y = currentnode[1] + b
			newnode = (x,y)
			if newnode in closedlist or x < 0 or x > len(board) - 1 or y < 0 or y > len(board) - 1 or board[x][y] == '|' :
				continue
			elif newnode not in openlist :
				openlist.append(newnode)
				nodes[newnode] = [currentnode,nodes[currentnode][1] + 1]
			elif newnode not in nodes or nodes[newnode][1] > nodes[currentnode][1] + 1 :
				nodes[newnode] = [currentnode,nodes[currentnode][1] + 1]
	if currentnode != end :
		return None , closedlist
	parent = nodes[end][0]
	path = [end]
	while parent != start :
		path.append(parent)
		parent = nodes[parent][0]
	return path

def DRAW() :

	route = ASTAR(start,end)
	for i,j in route :
		BLOCKS(board)
		pygame.draw.rect(SD,GREEN,(j * 32,i * 32,32,32))
		pygame.display.update()


RUN = True

while RUN :

	SD.fill(WHITE)

	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			RUN = False
		elif event.type == pygame.KEYDOWN :
			if event.key == pygame.K_RETURN :
				DRAW()
				time.sleep(10)
				RUN = False

	BLOCKS(board)
	pygame.display.update()

pygame.quit()
quit()