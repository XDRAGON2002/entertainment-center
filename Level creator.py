import pygame

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

SD = pygame.display.set_mode((600,600))
pygame.display.set_caption('LEVEL CREATOR')
SD.fill(WHITE)

def BLOCK(x,y) :

	pygame.draw.rect(SD,BLACK,(x,y,100,100))

board = [[1,0,1,0,1,0],
		 [0,1,0,1,0,1],
		 [1,0,1,0,1,0],
		 [0,1,0,1,0,1],
		 [1,0,1,0,1,0],
		 [0,1,0,1,0,1]]

for i,j in enumerate(board) :

	for k,l in enumerate(j) :

		if l == 1 :
			BLOCK(k * 100,i * 100)

a = True

while a :

	for i in pygame.event.get() :

		if i.type == pygame.QUIT :
			a = False


	pygame.display.update()

pygame.quit()
quit()