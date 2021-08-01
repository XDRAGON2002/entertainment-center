import pygame

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

SD = pygame.display.set_mode((400,400))
SD.fill(WHITE)
pygame.display.set_caption(' TIC TAC TOE ! ')
pygame.draw.rect(SD,BLACK,(130,0,5,400))
pygame.draw.rect(SD,BLACK,(265,0,5,400))
pygame.draw.rect(SD,BLACK,(0,130,400,5))
pygame.draw.rect(SD,BLACK,(0,265,400,5))
pygame.display.update()

def MESSAGE(TEXT) :
    
    F = pygame.font.Font('freesansbold.ttf',50)
    SD.blit(F.render(TEXT,True,BLACK),(80,150))
    pygame.display.update()

def LOOP() :

    A = 0
    AAG = ABG = ACG = BAG = BBG = BCG = CAG = CBG = CCG = 0
    AAR = ABR = ACR = BAR = BBR = BCR = CAR = CBR = CCR = 0
    CLR = 0

    while A == 0 :

        CR = pygame.mouse.get_pos()

        for I in pygame.event.get() :
            
            if I.type == pygame.QUIT :
                A = 1

            if 130 > CR[0] > 0 and 130 > CR[1] > 0 and I.type == pygame.MOUSEBUTTONDOWN :
                if I.button == 1 :
                    CLR = GREEN
                    AAG = 1
                elif I.button == 3 :
                    CLR = RED
                    AAR = 1
                pygame.draw.rect(SD,CLR,(0,0,130,130))
                
            if 265 > CR[0] > 135 and 130 > CR[1] > 0 and I.type == pygame.MOUSEBUTTONDOWN :
                if I.button == 1 :
                    CLR = GREEN
                    ABG = 1
                elif I.button == 3 :
                    CLR = RED
                    ABR = 1
                pygame.draw.rect(SD,CLR,(135,0,130,130))
                
            if 400 > CR[0] > 270 and 130 > CR[1] > 0 and I.type == pygame.MOUSEBUTTONDOWN :
                if I.button == 1 :
                    CLR = GREEN
                    ACG = 1
                elif I.button == 3 :
                    CLR = RED
                    ACR = 1
                pygame.draw.rect(SD,CLR,(270,0,130,130))
                
            if 130 > CR[0] > 0 and 265 > CR[1] > 135 and I.type == pygame.MOUSEBUTTONDOWN :
                if I.button == 1 :
                    CLR = GREEN
                    BAG = 1
                elif I.button == 3 :
                    CLR = RED
                    BAR = 1
                pygame.draw.rect(SD,CLR,(0,135,130,130))
                
            if 265 > CR[0] > 135 and 265 > CR[1] > 135 and I.type == pygame.MOUSEBUTTONDOWN :
                if I.button == 1 :
                    CLR = GREEN
                    BBG = 1
                elif I.button == 3 :
                    CLR = RED
                    BBR = 1
                pygame.draw.rect(SD,CLR,(135,135,130,130))
                
            if 400 > CR[0] > 270 and 265 > CR[1] > 135 and I.type == pygame.MOUSEBUTTONDOWN :
                if I.button == 1 :
                    CLR = GREEN
                    BCG = 1
                elif I.button == 3 :
                    CLR = RED
                    BCR = 1
                pygame.draw.rect(SD,CLR,(270,135,130,130))
                
            if 130 > CR[0] > 0 and 400 > CR[1] > 270 and I.type == pygame.MOUSEBUTTONDOWN :
                if I.button == 1 :
                    CLR = GREEN
                    CAG = 1
                elif I.button == 3 :
                    CLR = RED
                    CAR = 1
                pygame.draw.rect(SD,CLR,(0,270,130,130))
                
            if 265 > CR[0] > 135 and 400 > CR[1] > 270 and I.type == pygame.MOUSEBUTTONDOWN :
                if I.button == 1 :
                    CLR = GREEN
                    CBG = 1
                elif I.button == 3 :
                    CLR = RED
                    CBR = 1
                pygame.draw.rect(SD,CLR,(135,270,130,130))
                
            if 400 > CR[0] > 270 and 400 > CR[1] > 270 and I.type == pygame.MOUSEBUTTONDOWN :
                if I.button == 1 :
                    CLR = GREEN
                    CCG = 1
                elif I.button == 3 :
                    CLR = RED
                    CCR = 1
                pygame.draw.rect(SD,CLR,(270,270,130,130))

        pygame.display.update()

        if AAG == 1 and ABG == 1 and ACG == 1 :
            MESSAGE(' G  WINS !')
        elif BAG == 1 and BBG == 1 and BCG == 1 :
            MESSAGE(' G  WINS !')
        elif CAG == 1 and CBG == 1 and CCG == 1 :
            MESSAGE(' G  WINS !')
        elif AAG == 1 and BAG == 1 and CAG == 1 :
            MESSAGE(' G  WINS !')
        elif ABG == 1 and BBG == 1 and CBG == 1 :
            MESSAGE(' G  WINS !')
        elif ACG == 1 and BCG == 1 and CCG == 1 :
            MESSAGE(' G  WINS !')
        elif AAG == 1 and BBG == 1 and CCG == 1 :
            MESSAGE(' G  WINS !')
        elif ACG == 1 and BBG == 1 and CAG == 1 :
            MESSAGE(' G  WINS !')
            
        if AAR == 1 and ABR == 1 and ACR == 1 :
            MESSAGE(' R  WINS !')
        elif BAR == 1 and BBR == 1 and BCR == 1 :
            MESSAGE(' R  WINS !')
        elif CAR == 1 and CBR == 1 and CCR == 1 :
            MESSAGE(' R  WINS !')
        elif AAR == 1 and BAR == 1 and CAR == 1 :
            MESSAGE(' R  WINS !')
        elif ABR == 1 and BBR == 1 and CBR == 1 :
            MESSAGE(' R  WINS !')
        elif ACR == 1 and BCR == 1 and CCR == 1 :
            MESSAGE(' R  WINS !')
        elif AAR == 1 and BBR == 1 and CCR == 1 :
            MESSAGE(' R  WINS !')
        elif ACR == 1 and BBR == 1 and CAR == 1 :
            MESSAGE(' R  WINS !')


LOOP()
        
pygame.quit()

quit()
