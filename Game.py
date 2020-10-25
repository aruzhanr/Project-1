import pygame
import pickle
n=0
pygame.init()
size = (790, 480)
grey=(173,173,173)
fps = 20
owl0=pygame.image.load("owl0.jpg")
p=pygame.image.load("post2.jpg")
owl0= pygame.transform.scale(owl0, (200,200))
p= pygame.transform.scale(p, (300,200))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False
x=790
y=480
u=' Hello newbie, congratulations on your new job. '
t=''
done2=False
level=3
done3=True
while done3:
 while not done:
   screen.fill(grey)
   screen.blit(owl0, (0.75*x,0.58*y))
   screen.blit(p, (0.3*x,0.05*y))
   fontObj = pygame.font.Font('freesansbold.ttf', 20)
   textSurfaceObj = fontObj.render(u, True, [10,10,10])
   textRectObj = textSurfaceObj.get_rect()
   textRectObj.center = (0.3*x, 0.58*y)
   screen.blit(textSurfaceObj, textRectObj)
   textSurfaceObj2 = fontObj.render(" Your job is delivering mail.Beware of obstacles.Don't fall.  ", True, [10,10,10])
   textRectObj2 = textSurfaceObj2.get_rect()
   textRectObj2.center = (0.36*x, 0.65*y)
   screen.blit(textSurfaceObj2, textRectObj2)
   button1 = pygame.Rect(0.25*x,0.7*y ,200,40)
   pygame.draw.rect(screen,[220,220,220], button1)
   button2 = pygame.Rect(0.25*x,0.83*y,200,40)
   pygame.draw.rect(screen,[220,220,220], button2)
   textSurfaceObj3 = fontObj.render("Continue", True, [10,10,10])
   textRectObj3 = textSurfaceObj3.get_rect()
   textRectObj3.center = (0.38*x, 0.74*y)
   screen.blit(textSurfaceObj3, textRectObj3)
   textSurfaceObj4 = fontObj.render("Quit", True, [10,10,10])
   textRectObj4 = textSurfaceObj4.get_rect()
   textRectObj4.center = (0.37*x, 0.87*y)
   screen.blit(textSurfaceObj4, textRectObj4)
   
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            done3=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 0.25*x<=event.pos[0]<=0.25*x+200  and 0.7*y <=event.pos[1]<=0.7*y+40 :
                    done=True
                    done2=True
                elif 0.25*x<=event.pos[0]<=0.25*x+200  and 0.83*y <=event.pos[1]<=0.83*y+40 :
                    done=True
                    done3=False
   pygame.display.flip()
   clock.tick(fps)
 city=pygame.image.load("city.jpg")
 lock=pygame.image.load("lock.png")
 boat=pygame.image.load("boat.jpg")
 castle=pygame.image.load("castle.png")
 city= pygame.transform.scale(city, (150,150))
 lock= pygame.transform.scale(lock, (150,150))
 boat= pygame.transform.scale(boat, (150,150))
 castle= pygame.transform.scale(castle, (150,150))
 dy=5
 with open('data.pickle', 'rb') as f:
    level= pickle.load(f)
    print("ok")
    
 while done2==True:
    
        screen.fill((255,255,255))
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              done2 = False
          elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 0.4*x<=event.pos[0]<=0.4*x+150  and 0.65*y <=event.pos[1]<=0.65*y+40 and level>1 :
                    print("level-2")
                elif 0.1*x<=event.pos[0]<=0.1*x+150  and 0.85*y <=event.pos[1]<=0.85*y+40 :
                    print("level-1")
                elif 0.7*x<=event.pos[0]<=0.7*x+150  and 0.45*y <=event.pos[1]<=0.45*y+40 and level>2 :
                    print("level-3")
                elif 0.7*x<=event.pos[0]<=0.7*x+150  and 0.7*y <=event.pos[1]<=0.7*y+40 :
                    level=1
                elif 0.7*x<=event.pos[0]<=0.7*x+150  and 0.8*y <=event.pos[1]<=0.8*y+40 :
                    done2=False
                    done=False
        if level==1:
            screen.blit(city, (0.1*x,0.5*y))
            screen.blit(lock, (0.4*x,0.3*y))
            screen.blit(lock, (0.7*x,0.1*y))
        elif n==1 :
            gravity=-10
            if dy>=-100:
             if level==2:
                dy=dy-gravity
                screen.blit(city, (0.1*x,0.5*y))
                screen.blit(boat, (0.4*x,0.3*y))
                screen.blit(lock, (0.4*x,0.3*y+dy))
                screen.blit(lock, (0.7*x,0.1*y))
             elif level==3:
                dy=dy-gravity
                screen.blit(city, (0.1*x,0.5*y))
                screen.blit(boat, (0.4*x,0.3*y))
                screen.blit(castle, (0.7*x,0.1*y))
                screen.blit(lock, (0.7*x,0.1*y+dy))
            else:
                dy=5
                n=0
        elif level==2:
            screen.blit(city, (0.1*x,0.5*y))
            screen.blit(boat, (0.4*x,0.3*y))
            screen.blit(lock, (0.7*x,0.1*y))
        elif level==3:
            screen.blit(city, (0.1*x,0.5*y))
            screen.blit(boat, (0.4*x,0.3*y))
            screen.blit(castle, (0.7*x,0.1*y))
        button3 = pygame.Rect(0.1*x,0.85*y ,150,40)
        pygame.draw.rect(screen,[255,246,143], button3)
        button4 = pygame.Rect(0.4*x,0.65*y ,150,40)
        pygame.draw.rect(screen,[255,246,143] , button4)
        button5 = pygame.Rect(0.7*x,0.45*y ,150,40)
        pygame.draw.rect(screen,[255,246,143], button5)
        button6 = pygame.Rect(0.7*x,0.7*y ,150,40)
        pygame.draw.rect(screen,[211,211,211] , button6)
        button7 = pygame.Rect(0.7*x,0.8*y ,150,40)
        pygame.draw.rect(screen,[211,211,211], button7)
        textSurfaceObj3 = fontObj.render("Level-1", True, [10,10,10])
        textRectObj3 = textSurfaceObj3.get_rect()
        textRectObj3.center = (0.19*x, 0.89*y)
        screen.blit(textSurfaceObj3, textRectObj3)
        textSurfaceObj4 = fontObj.render("Level-2", True, [10,10,10])
        textRectObj4 = textSurfaceObj4.get_rect()
        textRectObj4.center = (0.49*x, 0.69*y)
        screen.blit(textSurfaceObj4, textRectObj4)
        textSurfaceObj5 = fontObj.render("Level-3", True, [10,10,10])
        textRectObj5 = textSurfaceObj5.get_rect()
        textRectObj5.center = (0.79*x, 0.49*y)
        screen.blit(textSurfaceObj5, textRectObj5)
        textSurfaceObj6 = fontObj.render("Delete progress", True, [10,10,10])
        textRectObj6 = textSurfaceObj6.get_rect()
        textRectObj6.center = (0.795*x, 0.74*y)
        screen.blit(textSurfaceObj6, textRectObj6)
        textSurfaceObj7 = fontObj.render("Back ", True, [10,10,10])
        textRectObj7 = textSurfaceObj7.get_rect()
        textRectObj7.center = (0.79*x, 0.84*y)
        screen.blit(textSurfaceObj7, textRectObj7)
        
                 
        level=1
        with open('data.pickle', 'wb') as f:
             pickle.dump(level, f) 
        pygame.display.flip()
        clock.tick(fps)
pygame.quit()
