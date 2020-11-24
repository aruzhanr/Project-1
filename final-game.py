
import pygame
import pickle
import random
import time

done3=True #ойыннын озине жауап берип тур
done = False #bastaldy 1-shi okoshko
done2 = False #bastaldy 2-shi okoshko
LEVEL1GOAL=False #для переходного скрина
n=0
LEVEL1= False
Level2=False
Level3=False
GameOver=False
Cong=False

pygame.init()
size = (790, 480)
grey=(173,173,173)
fps = 20 #frame per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock() 

#loading images
post=pygame.image.load("post2.jpg")
post= pygame.transform.scale(post, (200,90))
back=pygame.image.load("maxresdefault.jpg")
back=pygame.transform.scale(back,(790,480))

x=790
y=480

t='' 

class B2:
     def init(self,bx,by):
         self.bx = bx
         self.by = by
     def fly(self,bbird1,bbird2,bbird3,i):
         lst_cls=[]
         if i<=5:
             i=i+1
             lst_cls.append(bbird1)
             lst_cls.append(i)
         elif i<=10:
             i=i+1
             lst_cls.append(bbird2)
             lst_cls.append(i)
         elif i<=15:
              if i==15:
                  i=0
              else:
                  i=i+1
              lst_cls.append(bbird3)
              lst_cls.append(i)
         return(lst_cls) #[bbird3,1,bbird3,2,bbird3,3,bbird3,4,bbird3,5]
     def change_direction(self,y1,bn,by):
          if y1-by>5:
              dy2=5*bn
          elif y1-by<5 or y1-by>-5:
              dy2=0
          else:
              dy2=-5*bn
          by=by+dy2
          return(by)
     def ghost_ab(self,gy2,gy3):
          lst_gh=[]
          
          if gy-gy2<=150:
             gy2=gy2-5
             gy3=gy3+5
             lst_gh.append(gy2)
             lst_gh.append(gy3)
          else:
             lst_gh.append(gy2)
             lst_gh.append(gy3)
          return(lst_gh)
pygame.mixer.music.load('03 Before School 1.mp3')
pygame.mixer.music.play()
while done3: #true
 while not done: #false
   
   
   screen.fill(grey)
   screen.blit(back, (0,0))
   screen.blit(post, (0.3*x+0.3*x+100,0.05*y+350))
   fontObj = pygame.font.Font('ChunkFive-Regular.otf', 20) # файл .ttf, который расшифровывается как True Type File.
   fontaig= pygame.font.Font('ChunkFive-Regular.otf', 100)
  
   textSurfaceObj2 = fontaig.render("Welcome! ", True, (153, 0, 153))
   textRectObj2 = textSurfaceObj2.get_rect() #get rectangular area
   textRectObj2.center = (0.36*x+110, 0.65*y-220)
   screen.blit(textSurfaceObj2, textRectObj2)
   button1 = pygame.Rect(0.25*x+100,0.7*y-100 ,200,40)
   pygame.draw.rect(screen,[220,220,220], button1)
   button2 = pygame.Rect(0.25*x+100,0.83*y-100,200,40)
   pygame.draw.rect(screen,[220,220,220], button2)
   textSurfaceObj3 = fontObj.render("Continue", True, (0, 0, 255))
   textRectObj3 = textSurfaceObj3.get_rect()
   textRectObj3.center = (0.38*x+100, 0.74*y-100)
   screen.blit(textSurfaceObj3, textRectObj3)
   textSurfaceObj4 = fontObj.render("Quit", True, (0, 0, 255))
   textRectObj4 = textSurfaceObj4.get_rect()
   textRectObj4.center = (0.37*x+100, 0.87*y-100)
   screen.blit(textSurfaceObj4, textRectObj4)
   
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            done3=False
           
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 0.25*x+100<=event.pos[0]<=0.25*x+300  and 0.7*y-100 <=event.pos[1]<=0.7*y-60:
                    done=True
                    done2=True #bastaldy ekinshi okoshko
                elif 0.25*x+100<=event.pos[0]<=0.25*x+300  and 0.83*y-100 <=event.pos[1]<=0.83*y-60 :
                    done=True
                    done3=False
             
   pygame.display.flip() #obnovlyaet
   clock.tick(fps)
 mapp=pygame.image.load("big_map.png")
 mapp= pygame.transform.scale(mapp, (790,480))
 url=pygame.image.load("url.png")
 url= pygame.transform.scale(url, (790,480))
 city=pygame.image.load("round.png")
 lock=pygame.image.load("lock.jpeg")
 boat=pygame.image.load("bbird3.png")
 castle=pygame.image.load("castle.jpeg")
 city= pygame.transform.scale(city, (150,150))
 lock= pygame.transform.scale(lock, (150,150))
 boat= pygame.transform.scale(boat, (150,150))
 castle= pygame.transform.scale(castle, (150,150))
 dy=5 ###########################dy mynda
 try:
  with open('data.pickle', 'rb') as f:
    level= pickle.load(f)
    print("ok")
 except FileNotFoundError:
     level=1
    
     
 while done2==True:   
        level=3
        screen.fill((255,255,255))
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              done2 = False
              done3=False
              
          elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 0.1*x<=event.pos[0]<=0.1*x+150  and 0.85*y <=event.pos[1]<=0.85*y+40 :
                    done2=False
                    LEVEL1GOAL=True
                    LEVEL=1
                elif 0.4*x<=event.pos[0]<=0.4*x+150  and 0.65*y <=event.pos[1]<=0.65*y+40 and level>1 :
                    LEVEL1GOAL=True
                    done2=False
                    LEVEL=2
                elif 0.7*x<=event.pos[0]<=0.7*x+150  and 0.45*y <=event.pos[1]<=0.45*y+40 and level>2 :
                    done2=False
                    LEVEL1GOAL=True
                    LEVEL=3
                elif 0.7*x<=event.pos[0]<=0.7*x+150  and 0.7*y <=event.pos[1]<=0.7*y+40 :
                    level=1
                elif 0.7*x<=event.pos[0]<=0.7*x+150  and 0.8*y <=event.pos[1]<=0.8*y+40 :
                    done2=False
                    done=False
        screen.blit(mapp,(0,0))             
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
                screen.blit(lock, (0.4*x,0.3*y+dy))###########################################
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

        with open('data.pickle', 'wb') as f:
             pickle.dump(level, f) 
        pygame.display.flip()
        clock.tick(fps)
 delo=pygame.image.load("delo.jpg")
 delo= pygame.transform.scale(delo, (790,480))
 bird1=pygame.image.load("bird1.jpg")
 bird1= pygame.transform.scale(bird1, (50,50))
 bird2=pygame.image.load("bird2.jpg")
 bird2= pygame.transform.scale(bird2, (50,50))
 bird3=pygame.image.load("bird3.jpg")
 bird3= pygame.transform.scale(bird3, (50,50))
 house=pygame.image.load("house.jpg")
 house= pygame.transform.scale(house, (150,350))
 cloud=pygame.image.load("verto.png")
 cloud= pygame.transform.scale(cloud, (150,70))
 
 i=0
 gravity=1.5
 dy=-5
 start=0
 movement=100
 displ=0
 lst=[] #object or cloud choosing
 lst2=[] #x coord
 lst3=[] #y coord
 p=100
 lst4=[] #letter's y
 lst5=[] #letter's x
 let=150
 score=0
 letter=pygame.image.load("post2.jpg")
 letter= pygame.transform.scale(letter, (20,20))
 letter2= pygame.transform.scale(letter, (200,100))
 ilom=pygame.image.load("ilom.png")
 #letter= pygame.transform.scale(letter, (790,480))

 while LEVEL1GOAL:
     pygame.mixer.music.stop()
     #screen.fill(grey)
     screen.blit(ilom,(0,0))
     screen.blit(letter2, (0.45*x,0.47*y))
     buttonGO=pygame.Rect(0.3*x,0.8*y ,150,40)
     pygame.draw.rect(screen,[255,246,143], buttonGO)
     fontObj6 = pygame.font.Font('freesansbold.ttf', 40)
     textSurfaceObj16 = fontObj6.render("GOAL", True, (153,0,153))
     textRectObj16 = textSurfaceObj16.get_rect()
     textRectObj16.center = (0.2*x, 0.2*y)
     screen.blit(textSurfaceObj16, textRectObj16)
     fontObj7 = pygame.font.Font('freesansbold.ttf', 150)
     textSurfaceObj17 = fontObj7.render("10*", True, [10,10,10])
     textRectObj17 = textSurfaceObj17.get_rect()
     textRectObj17.center = (0.3*x, 0.6*y)
     screen.blit(textSurfaceObj17, textRectObj17)
     textSurfaceObj18 = fontObj.render("GO", True, (153,0,153))
     textRectObj18 = textSurfaceObj18.get_rect()
     textRectObj18.center = (0.4*x, 0.85*y)
     screen.blit(textSurfaceObj18, textRectObj18)
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              done3=False
              LEVEL1GOAL=False
          elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 0.3*x<=event.pos[0]<=0.3*x+150  and 0.8*y <=event.pos[1]<=0.8*y+40 :
                    if LEVEL==1:
                       LEVEL1GOAL=False
                       LEVEL1=True
                    elif LEVEL==2:
                        LEVEL1GOAL=False
                        Level2=True
                    elif LEVEL==3:
                         LEVEL1GOAL=False
                         Level3=True
     pygame.display.flip()
     clock.tick(fps)     
     
 while LEVEL1:
      
     screen.fill((132,217,217))
     #screen.blit(delo,(0,0))
     
     goal=10
     if movement==p:
         
         obj=random.randint(1, 2) #house or cloud
         dx=0
         ldx=0
         if p%200==0:
             letr=random.randint(1,9)
             letr=letr*0.1
             lst4.append(letr)
             lst5.append(ldx)
         else:
          if obj==1:
             z=house
             r=random.randint(4,8)
             r=r*0.1
            
          elif obj==2:
             z=cloud
             r=random.randint(1,3)
             r=r*0.1
          lst.append(z)
          lst2.append(dx)
          lst3.append(r)
         p=p+50  
     movement=movement+1
  
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              LEVEL1= False
              done3=False
              GameOver=False
          elif event.type == pygame.KEYDOWN:     
              if event.key == pygame.K_SPACE :
                 start=1
                 dy=dy-20
                 #pygame.mixer.music.load('sfx-4.mpeg')
                 #pygame.mixer.music.play()
                
     dy = dy + gravity
     if start!=1:
         dy=0
         movement=0
     if 0.3*y+dy+50>480 or 0.3*y+dy<0:
         LEVEL1=False
         GameOver=True
     if i<=5:
         screen.blit(bird1, (0.1*x,0.3*y+dy))
         i=i+1
         bird=bird1
     elif i<=10:
         screen.blit(bird2, (0.1*x,0.3*y+dy))
         i=i+1
         bird=bird2
     elif i<=15:
         screen.blit(bird3, (0.1*x,0.3*y+dy))
         bird=bird3
         if i==15:
              i=0
         else:
              i=i+1
     for j in range(0,len(lst2)):
       
       if j!=len(lst2):
         screen.blit(lst[j], (x-lst2[j],lst3[j]*y))
         
         rect2 = pygame.Rect((0.1*x,0.3*y+dy , 50,50))
         if lst[j]==house:
             rect1=pygame.Rect((x-lst2[j] ,lst3[j]*y , 150, 350))
         else:
             rect1=pygame.Rect((x-lst2[j] ,lst3[j]*y , 150, 70))
         if rect1.colliderect(rect2):
                    LEVEL1=False
                    GameOver=True
                    
         
         if x-lst2[j]+200<0:
               del lst[j]
               del lst2[j]
               del lst3[j]
         else:
               lst2[j]=lst2[j]+5
       else:
           for j in range(0,len(lst2)):
               screen.blit(lst[j], (x-lst2[j],lst3[j]*y))
     for let in range(0,len(lst4)):
         screen.blit(letter, (x-lst5[let],lst4[let]*y))
         lst5[let]=lst5[let]+5
         rect3=pygame.Rect((x-lst5[let],lst4[let]*y , 20, 20))
         rect2 = pygame.Rect((0.1*x,0.3*y+dy , 50, 50))
         if rect3.colliderect(rect2):
                 score=score+1
                 lst5[let]=x+20
     fontObj5 = pygame.font.Font('freesansbold.ttf', 40)
     score=str(score)
     textSurfaceObj15 = fontObj5.render(score, True, [10,10,10])
     textRectObj15 = textSurfaceObj15.get_rect()
     textRectObj15.center = (0.9*x, 0.1*y)
     screen.blit(textSurfaceObj15, textRectObj15)
     score=int(score)
     if score==goal:
         Cong=True
         LEVEL1=False
     pygame.display.flip()
     clock.tick(fps)
 bbird1=pygame.image.load("bbird1.png")
 bbird1= pygame.transform.scale(bbird1, (50,50))
 bbird2=pygame.image.load("bbird2.png")
 bbird2= pygame.transform.scale(bbird2, (50,50))
 bbird3=pygame.image.load("bbird3.png")
 bbird3= pygame.transform.scale(bbird3, (50,50))
 fl=0
 bn=1
 y12=0
 bx=0
 by=0
 bird12=pygame.image.load("bird12.jpg")
 bird12= pygame.transform.scale(bird12, (50,50))
 bird22=pygame.image.load("bird22.png")
 bird22= pygame.transform.scale(bird22, (50,50))
 bird32=pygame.image.load("bird32.png")
 bird32= pygame.transform.scale(bird32, (50,50))
 cloud2=pygame.image.load("cloud2.png")
 cloud2= pygame.transform.scale(cloud2, (150,70))

 while Level2:
    goal=10
    screen.fill((16,78,139))
    if movement==p:
         
         
         dx=0
         
         ldx=0
         if p%300==0:
             letr=random.randint(1,9)
             letr=letr*0.1
             lst4.append(letr)
             lst5.append(ldx)
         elif p%150==0:
             bn=1
             bx=0
             by=random.randint(1,9)
             by=by*0.1
             y12=0
             
         
            
         else :
             z=cloud2
             r=random.randint(1,9)
             r=r*0.1
          
             lst2.append(dx)
             lst3.append(r)
     
         p=p+50
    movement=movement+1
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              Level2= False
              done3=False
              GameOver=False
          elif event.type == pygame.KEYDOWN:     
              if event.key == pygame.K_SPACE :
                 start=1
                 dy=dy-20
                 #pygame.mixer.music.load('sfx-4.mpeg')
                 #pygame.mixer.music.play()
    dy = dy + gravity
    if 0.3*y+dy+50>480 or 0.3*y+dy<0:
         Level2=False
         GameOver=True
    if start!=1:
         dy=0
         movement=0
    
    if i<=5:
         screen.blit(bird12, (0.1*x,0.3*y+dy))
         i=i+1
         bird=bird12
    elif i<=10:
         screen.blit(bird22, (0.1*x,0.3*y+dy))
         i=i+1
         bird=bird22
    elif i<=15:
         screen.blit(bird32, (0.1*x,0.3*y+dy))
         bird=bird32
         if i==15:
              i=0
         else:
              i=i+1
    for j in range(0,len(lst2)):
       
       if j!=len(lst2):
         screen.blit(cloud2, (x-lst2[j],lst3[j]*y))
         
         rect2 = pygame.Rect((0.1*x,0.3*y+dy , 50, 50))
         rect1=pygame.Rect((x-lst2[j] ,lst3[j]*y , 150, 70))
         if rect1.colliderect(rect2):
                    Level2=False
                    GameOver=True
                    
         
         if x-lst2[j]+200<0:
              
               del lst2[j]
               del lst3[j]
         else:
               lst2[j]=lst2[j]+5
       else:
           for j in range(0,len(lst2)):
               screen.blit(cloud2, (x-lst2[j],lst3[j]*y))
    for let in range(0,len(lst4)):
         screen.blit(letter, (x-lst5[let],lst4[let]*y))
         lst5[let]=lst5[let]+5
         rect3=pygame.Rect((x-lst5[let],lst4[let]*y , 20, 20))
         rect2 = pygame.Rect((0.1*x,0.3*y+dy , 50, 50))
         if rect3.colliderect(rect2):
                 score=score+1
                 lst5[let]=x+20
    bbird5=B2()#(bx,by)
    bird=bbird5.fly( bbird1,bbird2,bbird3,fl)
    fl=bird[1]
    if x-bx<=x/2:
        if y12==0:
          y1=0.3*y+dy
          y12=1
        by=bbird5.change_direction(y1,bn,by)
        bn=bn+1
    screen.blit(bird[0], (x-bx,by))
    rect2 = pygame.Rect((0.1*x,0.3*y+dy , 50, 50))
    rect1=pygame.Rect((x-bx ,by , 50, 50))
    if rect1.colliderect(rect2):
                    Level2=False
                    GameOver=True
    bx=bx+5
    fontObj5 = pygame.font.Font('freesansbold.ttf', 40)
    score=str(score)
    textSurfaceObj15 = fontObj5.render(score, True, [10,10,10])
    textRectObj15 = textSurfaceObj15.get_rect()
    textRectObj15.center = (0.9*x, 0.1*y)
    screen.blit(textSurfaceObj15, textRectObj15)
    score=int(score)
    if score==goal:
         Cong=True
         Level2=False
    pygame.display.flip()
    clock.tick(fps)
 fl=0
 bn=1
 y12=0
 bx=0
 by=0
 i=0
 s=50
 gx=0
 gy=0
 y22=1
 u=0
 ob=4
 bh=0
 gh=0
 timer2=0
 timer=180
 ghost=pygame.image.load("ghost.png")
 ghost= pygame.transform.scale(ghost, (50,50))
 pygame.mixer.music.load('chasy_009.mpeg')
 pygame.mixer.music.play()
 pumpkin=pygame.image.load("jnk.png")
 pumpkin= pygame.transform.scale(pumpkin, (50,50))
 candy=pygame.image.load("candy.png")
 candy= pygame.transform.scale(candy, (50,50))
 pum=0
 candy_n=0
 can=0
 lst_can=[]
 lst_cany=[]
 rectp=pygame.Rect((0,0 , 20, 20))
 while Level3:################################################
    goal=5
    
    screen.fill((16,78,139))
    if s==60:
     if ob%10==0:
         px=0
         s=0
         pumy=random.randint(1,9)
         pumy=pumy*0.1*y
         pum=1
     elif ob%7==0:
         dx=0
         ldx=0
         letr=random.randint(1,9)
         letr=letr*0.1
         lst4.append(letr)
         lst5.append(ldx)
         s=0
       
     elif ob%5==0:
             y22=0
             
             gx=0
             gy=random.randint(3,5)
             gy=gy*0.1*y
             s=0
             u=1
             gh=1
     elif ob%4==0:
             bh=1
             bn=1
             bx=0
             by=random.randint(1,9)
             by=by*0.1
             y12=0
             s=0
       
     else  :
             dx=0
             z=cloud2
             r=random.randint(1,9)
             r=r*0.1
             s=0
             lst2.append(dx)
             lst3.append(r)
     ob=ob+1
    s=s+1
    movement=movement+1
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              Level3= False
              done3=False
              GameOver=False
          elif event.type == pygame.KEYDOWN:     
              if event.key == pygame.K_SPACE :
                 start=1
                 dy=dy-20
          elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if candy_n>0:
                     
                     candy_n=candy_n-1
                     can=1
                     lst_can.append(0.1*x)
                     lst_cany.append(0.3*y+dy)
    dy = dy + gravity
    if 0.3*y+dy+50>480 or 0.3*y+dy<0:
         Level3=False
         GameOver=True
    if start!=1:
         dy=0
         movement=0
    
    if i<=5:
         screen.blit(bird12, (0.1*x,0.3*y+dy))
         i=i+1
         bird=bird12
    elif i<=10:
         screen.blit(bird22, (0.1*x,0.3*y+dy))
         i=i+1
         bird=bird22
    elif i<=15:
         screen.blit(bird32, (0.1*x,0.3*y+dy))
         bird=bird32
         if i==15:
              i=0
         else:
              i=i+1
    for j in range(0,len(lst2)):
       
       if j!=len(lst2):
         screen.blit(cloud2, (x-lst2[j],lst3[j]*y))
         
         rect2 = pygame.Rect((0.1*x,0.3*y+dy , 50, 50))
         rect1=pygame.Rect((x-lst2[j] ,lst3[j]*y , 150, 70))
         if rect1.colliderect(rect2):
                    Level3=False
                    GameOver=True
                    
         if rectp.colliderect(rect1):
              lst3[j]=1000
         if x-lst2[j]+200<0:
              
               del lst2[j]
               del lst3[j]
         else:
               lst2[j]=lst2[j]+5
       else:
           for j in range(0,len(lst2)):
               screen.blit(cloud2, (x-lst2[j],lst3[j]*y))
    for let in range(0,len(lst4)):
         screen.blit(letter, (x-lst5[let],lst4[let]*y))
         lst5[let]=lst5[let]+5
         rect3=pygame.Rect((x-lst5[let],lst4[let]*y , 20, 20))
         rect2 = pygame.Rect((0.1*x,0.3*y+dy , 50, 50))
         if rect3.colliderect(rect2):
                 score=score+1
                 lst5[let]=x+20
         
    if bh==1:
      bbird5=B2()#(bx,by)
      bird=bbird5.fly( bbird1,bbird2,bbird3,fl)
      fl=bird[1]
      if x-bx<=x/2:
        if y12==0:
          y1=0.3*y+dy
          y12=1
        by=bbird5.change_direction(y1,bn,by)
        bn=bn+1
      screen.blit(bird[0], (x-bx,by))
      rect2 = pygame.Rect((0.1*x,0.3*y+dy , 50, 50))
      rect1=pygame.Rect((x-bx ,by , 50, 50))
      if rect1.colliderect(rect2):
                    Level3=False
                    GameOver=True
      if rectp.colliderect(rect1)  :
                    by=1000 
      bx=bx+5
    if pum==1:
         screen.blit(pumpkin, (x-px,pumy))
         px=px+5
         rect8 = pygame.Rect((0.1*x,0.3*y+dy , 50, 50))
         rect9=pygame.Rect((x-px ,pumy , 50, 50))
         if rect8.colliderect(rect9):
              pumy=1000
              candy_n=3
    ghost2=B2()#(gx,gy)
    if x-gx<=x/2:
        if y22==0:
            gy2=gy
            gy3=gy
            y22=1
        if u==1:
           gy4=ghost2.ghost_ab(gy2,gy3)
           gy2=gy4[0]
           gy3=gy4[1]
           screen.blit(ghost, (x-gx,gy4[0]))
           screen.blit(ghost, (x-gx,gy4[1]))
           rect3=pygame.Rect((x-gx ,gy2 , 50, 50))
           rect4=pygame.Rect((x-gx ,gy3 , 50, 50))
           rect1 = pygame.Rect((0.1*x,0.3*y+dy , 50, 50))
           if rect1.colliderect(rect3) or rect1.colliderect(rect4) :
                    Level3=False
                    GameOver=True
           if rectp.colliderect(rect3)  :
                    gy2=1000
           if rectp.colliderect(rect4)  :
                    gy3=1000 
    if gh==1:
      screen.blit(ghost, (x-gx,gy))
      rect1 = pygame.Rect((0.1*x,0.3*y+dy , 50, 50))
      rect2=pygame.Rect((x-gx ,gy , 50, 50))
     
      if rect1.colliderect(rect2)  :
                    Level3=False
                    GameOver=True
      if rectp.colliderect(rect2)  :
                    gy=1000         
      gx=gx+5
    if can==1:
         for can_num in range (len(lst_can)):
            screen.blit(candy, (lst_can[can_num],lst_cany[can_num]))
           
            rectp = pygame.Rect(( lst_can[can_num] ,lst_cany[can_num]  , 50, 50))
            lst_can[can_num]=lst_can[can_num]+10   
            
    fontObj5 = pygame.font.Font('freesansbold.ttf', 40)
    score=str(score)
    timer=str(timer)
    candy_n=str(candy_n)
    textSurfaceObj15 = fontObj5.render(score, True, [10,10,10])
    textRectObj15 = textSurfaceObj15.get_rect()
    textRectObj15.center = (0.9*x, 0.1*y)
    screen.blit(textSurfaceObj15, textRectObj15)
    textSurfaceObj18 = fontObj5.render(f'time:{timer}', True, [10,10,10])
    textRectObj18 = textSurfaceObj18.get_rect()
    textRectObj18.center = (0.85*x, 0.9*y)
    screen.blit(textSurfaceObj18, textRectObj18)
    textSurfaceObjc = fontObj5.render(candy_n, True, [10,10,10])
    textRectObjc = textSurfaceObjc.get_rect()
    textRectObjc.center = (0.85*x, 0.8*y)
    screen.blit(textSurfaceObjc, textRectObjc)
    timer=int(timer)
    score=int(score)
    candy_n=int(candy_n)
    timer2=timer2+1
    if timer2%20==0:
         timer=timer-1
    if score==goal:
         Cong=True
         Level2=False
    if timer==0:
         Level3=False
         GameOver=True
    pygame.display.flip()
    clock.tick(fps)
 pygame.mixer.music.stop()
 while Cong:
     screen.fill((255,255,255))
     fontObj8 = pygame.font.Font('freesansbold.ttf', 100)
     textSurfaceObj20 = fontObj8.render("Congartulation", True, [10,10,10])
     textRectObj20 = textSurfaceObj20.get_rect()
     textRectObj20.center = (0.5*x, 0.5*y)
     screen.blit(textSurfaceObj20, textRectObj20)
     buttonc = pygame.Rect(0.35*x,0.7*y ,200,40)
     pygame.draw.rect(screen,[220,220,220], buttonc)
     textSurfaceObj88 = fontObj.render("Continue", True, [10,10,10])
     textRectObj88 = textSurfaceObj88.get_rect()
     textRectObj88.center = (0.48*x, 0.74*y)
     screen.blit(textSurfaceObj88, textRectObj88)
     if level!=3:
       level=level+1
       n=1
     lst.clear()
     lst2.clear()
     lst3.clear()
     lst4.clear()
     lst5.clear()
     p=100
     movement=0
     i=0
     gravity=1.5
     dy=-5
     start=0
     with open('data.pickle', 'wb') as f:
             pickle.dump(level, f)
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              Cong=False
              done3=False
          elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 0.35*x<=event.pos[0]<=0.35*x+200  and 0.7*y <=event.pos[1]<=0.7*y+40 :
                  Cong=False
                  done2=True
                    
     pygame.display.flip()
     clock.tick(fps)
 gameover=pygame.image.load("game_over.jpeg")
 gameover= pygame.transform.scale(gameover, (300,300))
 #pygame.mixer.music.load('Sound_08426.mp3')
 #pygame.mixer.music.play()
 while GameOver:
     screen.fill((255,255,255))
     screen.blit(gameover, (0.3*x,0.05*y))
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              GameOver=False
              done3=False
          elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 0.34*x<=event.pos[0]<=0.34*x+250  and 0.63*y <=event.pos[1]<=0.63*y+60:
                    if LEVEL==1:
                        GameOver=False
                        LEVEL1=True
                    elif LEVEL==2:
                        GameOver=False
                        Level2=True
                    elif LEVEL==3:
                        GameOver=False
                        Level3=True
                
                elif 0.34*x<=event.pos[0]<=0.34*x+250  and 0.83*y <=event.pos[1]<=0.83*y+60 :
                    GameOver=False
                    done2=True
     button10 = pygame.Rect(0.34*x,0.63*y ,250,60)
     pygame.draw.rect(screen,grey, button10)
     button11 = pygame.Rect(0.34*x,0.83*y ,250,60)
     pygame.draw.rect(screen,grey, button11)
     fontObj2 = pygame.font.Font('freesansbold.ttf', 40)
     textSurfaceObj7 = fontObj2.render("Back ", True, [10,10,10])
     textRectObj7 = textSurfaceObj7.get_rect()
     textRectObj7.center = (0.5*x, 0.9*y)
     screen.blit(textSurfaceObj7, textRectObj7)
     textSurfaceObj8 = fontObj2.render("Start again", True, [10,10,10])
     textRectObj8 = textSurfaceObj8.get_rect()
     textRectObj8.center = (0.5*x, 0.7*y)
     screen.blit(textSurfaceObj8, textRectObj8)
    
     pygame.display.flip()
     clock.tick(fps)
 pygame.mixer.music.stop() 
 
      
     
     
pygame.quit()
