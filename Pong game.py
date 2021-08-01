import pygame
import numpy as np

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

SD = pygame.display.set_mode((800,600))
pygame.display.set_caption('PONG')
SD.fill(WHITE)

LY = 0
LC = 0
RY = 0
RC = 0
BX = 375
BVX = 0.4
BY = 275
BVY = -0.4

def LB(x,y) :

	pygame.draw.rect(SD,BLACK,(x,y,25,150))

def RB(x,y) :

	pygame.draw.rect(SD,BLACK,(x,y,25,150))

def BB(x,y) :

	pygame.draw.rect(SD,BLACK,(x,y,50,50))

a = True

while a :

	for i in pygame.event.get() :

		if i.type == pygame.QUIT :
			a = False

		elif i.type == pygame.KEYDOWN :
			if i.key == pygame.K_w :
				LC -= 0.5
			elif i.key == pygame.K_s :
				LC += 0.5
			elif i.key == pygame.K_UP :
				RC -= 0.5
			elif i.key == pygame.K_DOWN :
				RC += 0.5
		elif i.type == pygame.KEYUP :
			if i.key == pygame.K_w or i.key == pygame.K_s :
				LC = 0
			if i.key == pygame.K_UP or i.key == pygame.K_DOWN :
				RC = 0

	LY += LC
	RY += RC
	BX += BVX
	BY += BVY

	if LY < 0 :
		LY = 0
	elif LY > 450 :
		LY = 450

	if RY < 0 :
		RY = 0
	elif RY > 450 :
		RY = 450

	if BY < 0 or BY > 550 :
		BVY = -BVY

	if BX < 0 or BX >750 :
		BX = 375
		BVX = -BVX
		BY = 275
		BVY = -BVY

	if 675 < BX and RY < BY < RY + 150 :
		BVX = -BVX
	elif BX < 75 and LY < BY < LY + 150 :
		BVX = -BVX

	SD.fill(WHITE)
	LB(50,LY)
	RB(725,RY)
	BB(BX,BY)

	pygame.display.update()

pygame.quit()
quit()