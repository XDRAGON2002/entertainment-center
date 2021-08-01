import pygame
import random
import time
import math

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

SD = pygame.display.set_mode((600,600))
pygame.display.set_caption('BLOCK FALL')
SD.fill(WHITE)
CLK = pygame.time.Clock()
ST = time.time()

COLORS = [RED,GREEN,BLUE]
PCOLOR = BLACK
ECOLOR = [random.choice(COLORS),random.choice(COLORS),random.choice(COLORS),random.choice(COLORS)]
COUNT = [0,0,0,0]
CL2 = [0,0,0,0]
SCORE = 0
RESPAWN = 0
FPS = 60

PX = 275
PY = 450
PXC = 0
PYC = 0
EX = [random.randint(0,550),random.randint(0,550),random.randint(0,550),random.randint(0,550)]
EY = [0,50,100,150]
EXC = 0
EYC = 2

def PLAYER(x,y,COLOR) :

	CL1 = pygame.draw.rect(SD,COLOR,(x,y,50,50))
	return CL1

def ENEMY(x,y,COLOR,i) :

	CL2[i] = pygame.draw.rect(SD,COLOR,(x,y,50,50))
	return CL2[i]

def MESSAGE(TEXT,x,y) :
    
    F = pygame.font.Font('freesansbold.ttf',30)
    SD.blit(F.render(TEXT,True,BLACK),(x,y))

a = True
b = [True,True,True,True]
c = 0
d = [0,0,0,0]

while a :

	for i in pygame.event.get() :

		if i.type == pygame.QUIT :
			a = False

		elif i.type == pygame.KEYDOWN :

			if i.key == pygame.K_LEFT :
				PXC -= 7
			elif i.key == pygame.K_RIGHT :
				PXC += 7

			if i.key == pygame.K_a :
				PCOLOR = RED
				c = 1
			elif i.key == pygame.K_s :
				PCOLOR = GREEN
				c = 2
			elif i.key == pygame.K_d :
				PCOLOR = BLUE
				c = 3

		elif i.type == pygame.KEYUP :

			if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT :
				PXC = 0

	SD.fill(WHITE)

	PX += PXC

	if PX > 550 :
		PX = 550
	elif PX < 0 :
		PX = 0

	CL1 = PLAYER(PX,PY,PCOLOR)

	for i in range(0,4) :
		
		EY[i] += EYC
		
		if EY[i] > 500 :
			EY[i] = 0
		
		if b[i] :
			CL2[i] = ENEMY(EX[i],EY[i],ECOLOR[i],i)
			if ECOLOR[i] == RED :
				d[i] = 1
			elif ECOLOR[i] == GREEN :
				d[i] = 2
			elif ECOLOR[i] == BLUE :
				d[i] = 3

		if CL1.colliderect(CL2[i]) == 1 and c == d[i] :
			b[i] = False

		if not b[i] :
			COUNT[i] += 1
			if COUNT[i] >= FPS * RESPAWN :
				b[i] = True
				ECOLOR[i] = random.choice(COLORS)
				EX[i] = random.randint(0,550)
				EY[i] = 0
				COUNT[i] = 0
				SCORE += 1

	CLK.tick(FPS)
	FT = time.time() - ST
	MESSAGE('SCORE - ',0,0)
	MESSAGE(str(SCORE),130,0)
	MESSAGE('TIME - ',430,0)
	MESSAGE(str(math.floor(FT)),530,0)
	MESSAGE('RED - A     GREEN - S     BLUE - D',50,550)
	pygame.display.update()