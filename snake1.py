import pygame
import sys
import random
import time

check_errors=pygame.init()
if check_errors[1]>0:
    print("(!) Had {0} initializing errrors,exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

#play surface
playsurface=pygame.display.set_mode((700,500))
pygame.display.set_caption('Snake game!')

#colors
red=pygame.Color(255,0,0)#gameover
green=pygame.Color(0,255,0)#snnake
black=pygame.Color(0,0,0)#score
white=pygame.Color(255,255,255)#background
brown=pygame.Color(165,42,42)#food

#fps controller
fpscontroller=pygame.time.Clock()

#important variable
snakepos=[100,50]
snakebody=[[100,50],[90,50],[80,50]]
foodpos=[random.randrange(1,70)*10,random.randrange(1,48)*10]
foodspawn=True

direction='RIGHT'
changeto=direction
score=0
#game over function
def gameover():
    myfont=pygame.font.SysFont('algerian',50)
    gosurf=myfont.render('Game Over!',True,red)
    gorect=gosurf.get_rect()
    gorect.midtop=(350,20)
    playsurface.blit(gosurf,gorect)
    showscore(0)
    pygame.display.flip()

    time.sleep(4)
    
    pygame.quit()#pygame
    sys.exit()#console

def showscore(choice=1):
    sfont=pygame.font.SysFont('monaco',50)
    ssurf=sfont.render('score : {0}'.format(score),True,black)
    srect=ssurf.get_rect()
    if choice ==1:
        srect.midtop=(80,10)
    else:
        srect.midtop=(350,120)


    playsurface.blit(ssurf,srect)


#main logic code
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT or event.key==ord('d'):
                changeto='RIGHT'
            if event.key==pygame.K_LEFT or event.key==ord('a'):
                changeto='LEFT'
            if event.key==pygame.K_UP or event.key==ord('w'):
                changeto='UP'
            if event.key==pygame.K_DOWN or event.key==ord('s'):
                changeto='DOWN'
            if event.key==pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    #validation of direction
    if changeto=='RIGHT' and not direction=='LEFT':
        direction='RIGHT'
    if changeto=='LEFT' and not direction=='RIGHT':
        direction='LEFT'
    if changeto=='UP' and not direction=='DOWN':
        direction='UP'
    if changeto=='DOWN' and not direction=='UP':
        direction='DOWN'

    if direction=='RIGHT':
        snakepos[0]+=10
    if direction=='LEFT':
        snakepos[0]-=10
    if direction=='UP':
        snakepos[1]-=10
    if direction=='DOWN':
        snakepos[1]+=10


    #body mechanism
    snakebody.insert(0,list(snakepos))
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
        score+=1
        foodspawn= False
    else:
        snakebody.pop()
    if foodspawn== False:
        foodpos=[random.randrange(1,70)*10,random.randrange(1,49)*10]
    foodspawn=True
    
    playsurface.fill(white)
    #drw snake
    for pos in snakebody:
        pygame.draw.rect(playsurface,green, pygame.Rect(pos[0],pos[1],10,10))
        pygame.draw.rect(playsurface,brown, pygame.Rect(foodpos[0],foodpos[1],10,10))
    if snakepos[0]>710 or snakepos[0]<0:
        gameover()
    if snakepos[1]>490 or snakepos[1]<0:
        gameover()
    for block in snakebody[1:]:
        if snakepos[0]==block[0] and snakepos[1]==block[1]:
            gameover()
            
    showscore()

    pygame.display.flip()
    
    fpscontroller.tick(17)
    #pyinstaller
        
        


