import pygame
import time
import math
import random

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SD = pygame.display.set_mode((800,600))
SD.fill(WHITE)
pygame.display.set_caption('SNAKE')
CLK = pygame.time.Clock()

ST = time.time()
FPS = 60
COUNT = 0
RESPAWN = 0
SIZE = 0
SCORE = 0

CL3 = pygame.draw.rect(SD,WHITE,(0,0,0,0))

SX = 375
SXI = [0]
SY = 275
SYI = [0]
SXC = 0
SYC = 0
AX = random.randint(0,750)
AY = random.randint(0,550)

a = True
b = True
c = 0

def SNAKE(x,y) :

	CL1 = pygame.draw.rect(SD,GREEN,(x,y,50,50))
	return CL1

def APPLE(x,y) :

	CL2 = pygame.draw.rect(SD,RED,(x,y,50,50))
	return CL2

def LENGTH(x,y) :

	CL3 = pygame.draw.rect(SD,BLUE,(x,y,50,50))
	return CL3

def MESSAGE(TEXT,x,y) :
    
    F = pygame.font.Font('freesansbold.ttf',30)
    SD.blit(F.render(TEXT,True,BLACK),(x,y))

while a :

	for i in pygame.event.get() :

		if i.type == pygame.QUIT :
			a = False
		elif i.type == pygame.KEYDOWN :
			if i.key == pygame.K_LEFT :
				SXC = 0
				SYC = 0
				SXC -= 5
			elif i.key == pygame.K_RIGHT :
				SXC = 0
				SYC = 0
				SXC += 5
			elif i.key == pygame.K_UP :
				SXC = 0
				SYC = 0
				SYC -= 5
			elif i.key == pygame.K_DOWN :
				SXC = 0
				SYC = 0
				SYC += 5


	SX += SXC
	SY += SYC
	SXI[0] = SX
	SYI[0] = SY

	if SX < 0 or SX > 750 or SY < 0 or SY > 550 :
		a = False

	SD.fill(WHITE)

	if b :
		CL2 = APPLE(AX,AY)
	
	CL1 = SNAKE(SX,SY)

	if CL2.colliderect(CL1) == 1 :
		b = False
		SIZE += 1
		SCORE += 1
		SXI.append('0')
		SYI.append('0')
		AX = random.randint(0,750)
		AY = random.randint(0,550)

	for i in range(SIZE,0,-1) :
		SXI[i] = SXI[i - 1]
		SYI[i] = SYI[i - 1]
		if SXC == 5 :
			CL3 = LENGTH(SXI[i] - 50,SYI[i])
		elif SXC == -5 :
			CL3 = LENGTH(SXI[i] + 50,SYI[i])
		elif SYC == 5 :
			CL3 = LENGTH(SXI[i],SYI[i] - 50)
		elif SYC == -5 :
			CL3 = LENGTH(SXI[i],SYI[i] + 50)

	if CL3.colliderect(CL1) == 1 :
		a = False

	if not b :
		COUNT += 1 

	if COUNT >= FPS * RESPAWN :
		b = True
		COUNT = 0

	CLK.tick(FPS)

	FT = time.time() - ST
	MESSAGE('SCORE - ',0,0)
	MESSAGE(str(SCORE),130,0)
	MESSAGE('TIME - ',630,0)
	MESSAGE(str(math.floor(FT)),730,0)
	
	pygame.display.update()

pygame.quit()
quit()