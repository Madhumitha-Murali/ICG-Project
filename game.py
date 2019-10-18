import pygame
from PIL import Image
import time

pygame.init()

display_width=800
display_height=600
gray=(255,255,255)
red=(255,0,0)

gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Fruit Archer Game")

clock=pygame.time.Clock()
#archerimg=pygame.image.load('/home/madhumitha/ICG_Game/archer.jpg')
img = Image.open('/home/madhumitha/ICG_Game/archer.jpg')
bg  = Image.open('/home/madhumitha/ICG_Game/tree.jpeg')
width, height = img.size 
img = img.resize((width/4, height/4)) 
img = img.crop((0, 0, 119, 140)) 
width, height = bg.size 
bg = bg.resize((450, 200)) 
img.save("img_pygame.jpg") 
bg.save("bg_pygame.jpg") 
archerimg=pygame.image.load('/home/madhumitha/ICG_Game/img_pygame.jpg')
bgimg=pygame.image.load('/home/madhumitha/ICG_Game/bg_pygame.jpg')
#archerimg1=archerimg.resize((80,80),Image.NEAREST)

def text_objects(text,font):
    textsurface=font.render(text,True,red)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(7)
    game_loop()


def crash():
    message_display("YOU LOST")



def background():

    gamedisplays.blit(bgimg,(0,0))
    gamedisplays.blit(bgimg,(400,0))

def archer(x,y):
  
    gamedisplays.blit(archerimg,(x,y))
    

def game_loop():
   x=(display_width*0.4)
   y=(display_height*0.78)
   x_change=0
   y_change=0

   bumped=False
   while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and x>(-(display_width/2)):
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_UP:
                    y_change=-5
                if event.key==pygame.K_DOWN:
                    y_change=+5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    y_change=0

        x+=x_change
        y+=y_change
        gamedisplays.fill(gray)
        background()
        archer(x,y)
        if x>700 or x<-10:
            crash()
        pygame.display.update()
        clock.tick(60)

  

     #x+=x_change

game_loop()
pygame.quit()
quit()
