import pygame

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,140,0)
PURPLE = (128,0,128)

SD = pygame.display.set_mode((800,600))
SD.fill(WHITE)
pygame.display.set_caption('PAINT')

pygame.draw.rect(SD,BLACK,(600,0,100,100))
pygame.draw.rect(SD,WHITE,(700,0,100,100))
pygame.draw.rect(SD,RED,(600,100,100,100))
pygame.draw.rect(SD,GREEN,(700,100,100,100))
pygame.draw.rect(SD,BLUE,(600,200,100,100))
pygame.draw.rect(SD,YELLOW,(700,200,100,100))
pygame.draw.rect(SD,ORANGE,(600,300,100,100))
pygame.draw.rect(SD,PURPLE,(700,300,100,100))

pygame.draw.rect(SD,BLACK,(600,0,5,600))
pygame.draw.rect(SD,BLACK,(700,0,5,400))
pygame.draw.rect(SD,BLACK,(600,400,200,5))
pygame.draw.rect(SD,BLACK,(600,300,200,5))
pygame.draw.rect(SD,BLACK,(600,200,200,5))
pygame.draw.rect(SD,BLACK,(600,100,200,5))
pygame.draw.rect(SD,BLACK,(0,0,800,5))
pygame.draw.rect(SD,BLACK,(0,0,5,600))
pygame.draw.rect(SD,BLACK,(0,595,800,5))
pygame.draw.rect(SD,BLACK,(795,0,5,600))

pygame.display.update()

C = 0

def BRUSH(X,Y,COLOR) :
    
    pygame.draw.rect(SD,COLOR,(X,Y,20,20))

def LOOP1() :
    
    A = 0
    global C
    
    while A == 0 :
        
        CR = pygame.mouse.get_pos()

        for I in pygame.event.get() :

            if I.type == pygame.QUIT :
                A = 1

            elif I.type == pygame.MOUSEBUTTONDOWN :

                if I.button == 3 :
                    LOOP2()

            if I.type == pygame.MOUSEBUTTONDOWN :
                
                if 700 > CR[0] > 600 and 100 > CR[1] > 0 and I.button == 1 :

                    C = 0

                elif 800 > CR[0] > 700 and 100 > CR[1] > 0 and I.button == 1 :

                    C = 1

                elif 700 > CR[0] > 600 and 200 > CR[1] > 100 and I.button == 1 :

                    C = 2

                elif 800 > CR[0] > 700 and 200 > CR[1] > 100 and I.button == 1 :

                    C = 3

                elif 700 > CR[0] > 600 and 300 > CR[1] > 200 and I.button == 1 :

                    C = 4

                elif 800 > CR[0] > 700 and 300 > CR[1] > 200 and I.button == 1 :

                    C = 5

                elif 700 > CR[0] > 600 and 400 > CR[1] > 300 and I.button == 1 :

                    C = 6

                elif 800 > CR[0] > 700 and 400 > CR[1] > 300 and I.button == 1 :

                    C = 7
                   
            if 590 > CR[0] > 15 and 585 > CR[1] > 15 :

                if C == 0 :
                    
                    BRUSH(CR[0]-10,CR[1]-10,BLACK)

                if C == 1 :

                    BRUSH(CR[0]-10,CR[1]-10,WHITE)

                if C == 2 :
                    
                    BRUSH(CR[0]-10,CR[1]-10,RED)

                if C == 3 :
                    
                    BRUSH(CR[0]-10,CR[1]-10,GREEN)

                if C == 4 :
                    
                    BRUSH(CR[0]-10,CR[1]-10,BLUE)

                if C == 5 :
                    
                    BRUSH(CR[0]-10,CR[1]-10,YELLOW)

                if C == 6 :
                    
                    BRUSH(CR[0]-10,CR[1]-10,ORANGE)

                if C == 7 :
                    
                    BRUSH(CR[0]-10,CR[1]-10,PURPLE)

        pygame.display.update()

def LOOP2() :

    A = 0

    while A == 0 :

        CR = pygame.mouse.get_pos()
        
        for I in pygame.event.get() :

            if I.type == pygame.QUIT :
                A = 1

            elif I.type == pygame.MOUSEBUTTONDOWN :

                if I.button == 1 :
                    LOOP1()

        pygame.display.update()


LOOP2()

pygame.quit()
quit()
