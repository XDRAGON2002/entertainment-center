import math
import time
import random
import pygame

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SD = pygame.display.set_mode((800,600))
pygame.display.set_caption('TOP DOWN SHOOTER')
SD.fill(WHITE)
SD1 = pygame.Surface((100,100))
SD1.set_colorkey(BLACK)

CLK = pygame.time.Clock()
ST = time.time()
FPS = 60
COUNT = [0,0,0,0]
RESPAWN = 1
SCORE = 0

XP = 375
XC = 0
XPI = 0
YPI = 0
YP = 275
YC = 0
BX = 0
BY = 0
BVX = 0
BVY = 0
BVXI = 0
BVYI = 0
CRI = [0,0]
XE = [0,750,0,750]
YE = [0,0,550,550]
EVX = [3,3,3,3]
EVY = [3,3,3,3]
CL2 = [0,0,0,0]

CL3 = pygame.draw.rect(SD1,GREEN,(25,25,50,50))

def PLAYER(x,y) :

	R = SD.blit(SD1,(x,y))
	return R 	

def BULLET(x,y) :

	CL1 = pygame.draw.rect(SD,BLUE,(x,y,20,20))
	return CL1

def ENEMY(x,y,i) :

	CL2[i] = pygame.draw.rect(SD,RED,(x,y,50,50))
	return CL2[i]

def ANGLE(PX,PY,CX,CY) :

	AG = math.atan2(CY - (PY + 32),CX - (PX + 26))
	return AG 

def MESSAGE(TEXT,x,y) :
    
    F = pygame.font.Font('freesansbold.ttf',30)
    SD.blit(F.render(TEXT,True,BLACK),(x,y))

PLAYER(XP,YP)

FIRE = False

a = True
b = [True,True,True,True]

while a :

	CR = pygame.mouse.get_pos()

	for i in pygame.event.get() :

		if i.type == pygame.QUIT :
			a = False
		elif i.type == pygame.KEYDOWN :
			if i.key == pygame.K_w :
				YC -= 5
			elif i.key == pygame.K_a :
				XC -= 5
			elif i.key == pygame.K_s :
				YC += 5
			elif i.key == pygame.K_d :
				XC += 5
		elif i.type == pygame.KEYUP :
			if i.key == pygame.K_w or i.key == pygame.K_s :
				YC = 0
			elif i.key == pygame.K_a or i.key == pygame.K_d :
				XC = 0
		elif i.type == pygame.MOUSEBUTTONDOWN :
			if i.button == 1 :
				FIRE = True
				BX = XP + 15
				BY = YP + 15
				BVXI = BX
				BVYI = BY
				XPI = XP
				YPI = YP
				CRI[0] = CR[0]
				CRI[1] = CR[1]
				

	XP += XC
	YP += YC
	BX += BVX
	BY += BVY

	if XP > 750 :
		XP = 750
	elif XP < 0 :
		XP = 0

	if YP > 550 :
		YP = 550
	elif YP < 0 :
		YP = 0 

	R1 = PLAYER(XP - 25,YP - 25)
	OC = R1.center
	RS = pygame.transform.rotate(SD1,360 - ANGLE(XP - 25,YP - 25,CR[0],CR[1]) * 57.29)
	R2 = RS.get_rect()
	R2.center = OC

	SD.fill(WHITE)

	SD.blit(RS,R2)

	for i in range(0,4) :

		if b[i] :
			CL2[i] = ENEMY(XE[i],YE[i],i)
			XE[i] += EVX[i]
			YE[i] += EVY[i]

		if XE[i] > 750 or XE[i] < 0 :
			EVX[i] = -EVX[i]
		elif YE[i] > 550 or YE[i] < 0 :
			EVY[i] = -EVY[i]
		
		if FIRE :
			BVX = math.cos(ANGLE(XPI - 25,YPI - 25,CRI[0],CRI[1]))*10
			BVY = math.sin(ANGLE(XPI - 25,YPI - 25,CRI[0],CRI[1]))*10
			CL1 = BULLET(BX,BY)

			if CL2[i].colliderect(CL1) == 1 :
				b[i] = False
				XE[i] = random.randint(0,750)
				YE[i] = random.randint(0,550)

		if not b[i] :
			COUNT[i] += 1

		if COUNT[i] >= RESPAWN * FPS :
			b[i] = True
			COUNT[i] = 0
			SCORE += 1

	CLK.tick(FPS)
	FT = time.time() - ST
	MESSAGE('SCORE - ',0,0)
	MESSAGE(str(SCORE),130,0)
	MESSAGE('TIME - ',630,0)
	MESSAGE(str(math.floor(FT)),730,0)
	pygame.display.update()

pygame.quit()
quit()