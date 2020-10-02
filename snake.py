#IMPORTING ALL THE LIBRARIES NEEDED
import pygame
import random
from pygame.locals import*
import sys
import time

#CALLING THE CONSTRUCTOR
pygame.init()


#DIMENSIONS OF SCREEN
SH=500
SW=500

#SETTING UP SCREEN AND CAPTION
window=pygame.display.set_mode((SW,SH))
pygame.display.set_caption('SNAKE BY ANKIT')


#INITIALIZING THE CLOCK
clock=pygame.time.Clock()

#INTIALIZING THE FONT
font = pygame.font.Font(None,25)

#INCREASE THE LEN OF SNAKE
def plot_snake(window,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(window,color,[x,y,snake_size,snake_size])

#FUNCTION FOR SHOWING THE SCORE ON THE SCREEN
def text_screen(text,color,x,y):
    score_text=font.render(text,True,color)
    window.blit(score_text,[x,y])
def game_loop():
    #INITIALIZING COLOR
    white=(255,255,255)
    red=(255,0,0)
    black=(0,0,0)
    green=(0,255,0)

    #GAME VARIABLES
    snake_y=int(SH/2)#COORDINATES OF SNAKE
    snake_x=int(SW/2)#COORDINATES OF SNAKE
    vel_x=0#SPEED OF SNAKE
    vel_y=0#SPEED OF SNAKE
    snake_size=15#DIMENSIONS OF SNAKE

    game_over=False
    score=0

    #LIST FOR THE ICREMENT OF LENGHTH
    snk_list=[]
    snk_length=1

    apple_x=random.randint(10,SW/2)#COORDINATES OF THE FOOD(APPLE)
    apple_y=random.randint(10,SH/2)#COORDINATES OF THE FOOD(APPLE)
    fps=75
    while True:
        if game_over:
            time.sleep(2)
            window.fill(white)
            text_screen("GAME OVER! PRESS ENTER TO CONTINUE",black,70,250)
            for event in pygame.event.get():
                if event.type==KEYDOWN and event.key==K_RETURN:
                    game_loop()
                elif event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    pygame.quit()
                    sys.exit()
        else:
            #CHCEKS IF TO QUIT OR NOT
            for event in pygame.event.get():
                if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    pygame.quit()
                    sys.exit()

        #CHECKS FOR THE KEYPRESS AND MAKES THE SNAKE MOVE
                elif event.type==KEYDOWN:
                    if event.key==K_RIGHT:
                        if vel_x==-3:
                            break #SO THAT IT CANNOT MOVE DIRECTLY FROM LEFT TO RIGHT OR VICE VERSA
                        vel_x=3
                        vel_y=0

                    elif event.key==K_LEFT:
                        if vel_x==3:
                            break #SO THAT IT CANNOT MOVE DIRECTLY FROM LEFT TO RIGHT OR VICE VERSA
                        vel_x=-3
                        vel_y=0

                    elif event.key==K_UP:
                        if vel_y==3:
                            break #SO THAT IT CANNOT MOVE DIRECTLY FROM UP TO DOWN OR VICE VERSA
                        vel_x=0
                        vel_y=-3

                    elif event.key==K_DOWN:
                        if vel_y==-3:
                            break #SO THAT IT CANNOT MOVE DIRECTLY FROM UP TO DOWN OR VICE VERSA
                        vel_x=0
                        vel_y=3

            snake_x=snake_x+vel_x #CHANGES THE COORDINATES FOR EACH FRAME
            snake_y=snake_y+vel_y #CHANGES THE COORDINATES FOR EACH FRAME

            #CHACKS IF THE APPLE ATE OR NOT
            if (abs(snake_x-apple_x)<4 and abs(snake_y-apple_y)<4):
                score=score+1
                snk_length+=16
                apple_x=random.randint(10,SW/2) #MAKES A NEW APPLE 
                apple_y=random.randint(10,SH/2) #MAKES A NEW APPLE 
                
            window.fill(white)

            text_screen("score="+str(score),green,5,5)

            if snake_x<0:
                if vel_x!=0:
                    snake_x=SW
                elif vel_y!=0:
                    snake_y=SH
            elif snake_y<0:
                if vel_x!=0:
                    snake_x=SW
                elif vel_y!=0:
                    snake_y=SH
            elif snake_y>SH:
                if vel_x!=0:
                    snake_x=0
                elif vel_y!=0:
                    snake_y=0
            elif snake_x>SW:
                if vel_x!=0:
                    snake_x=0
                elif vel_y!=0:
                    snake_y=0

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True

            
            pygame.draw.rect(window,red,[apple_x,apple_y,snake_size,snake_size])
            plot_snake(window,red,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
game_loop()
