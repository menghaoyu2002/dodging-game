import pygame
from pathlib import Path
import random
import math

pygame.init()

#creates main surface
screen = pygame.display.set_mode((900,700))
pygame.display.set_caption('dodge')

#sets window icon
icon = pygame.image.load(str(Path.cwd()/'icon'/'icon.png'))
pygame.display.set_icon(icon)


class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, x, y, width, height):
        return self.sprite_sheet.subsurface((x, y, width, height))

#player class
class character:
    def __init__(self):
        self.state = 'alive'
        self.timer=0
        self.characterposx=425
        self.characterposy=300

        #down animation spritesheet creation
        spritepath = Path.cwd()/'Character'/'Character_Down.png'
        self.downframecount=0
        self.downframes=[]
        downsprite=SpriteSheet(str(spritepath))
        x=8
        for loop in range (4):
            frame=downsprite.get_image(x,7,16,21)
            x+=32
            self.downframes.append(frame)
        
        #down left animation spritesheet creation
        spritepath = Path.cwd()/'Character'/'Character_DownLeft.png'
        self.downleftframecount=0
        self.downleftframes=[]
        downleftsprite=SpriteSheet(str(spritepath))
        x=8
        for loop in range (4):
            frame=downleftsprite.get_image(x,6,15,21)
            x+=32
            self.downleftframes.append(frame)

        #down right animation spritesheet creation
        spritepath = Path.cwd()/'Character'/'Character_DownRight.png'
        self.downrightframecount=0
        self.downrightframes=[]
        downrightsprite=SpriteSheet(str(spritepath))
        x=9
        for loop in range (4):
            frame=downrightsprite.get_image(x,6,15,21)
            x+=32
            self.downrightframes.append(frame)
        
        #up animation spritesheet creation
        spritepath = Path.cwd()/'Character'/'Character_Up.png'
        self.upframecount=0
        self.upframes=[]
        upsprite = SpriteSheet(str(spritepath))
        x=8
        for loop in range (4):
            frame=upsprite.get_image(x,7,16,21)
            x+=32
            self.upframes.append(frame)
        
        #up left animation spritesheet creation
        spritepath = Path.cwd()/'Character'/'Character_UpLeft.png'
        self.upleftframecount=0
        self.upleftframes=[]
        upleftsprite = SpriteSheet(str(spritepath))
        x=8
        for loop in range (4):
            frame=upleftsprite.get_image(x,7,15,21)
            x+=32
            self.upleftframes.append(frame)
        
        #up right animation spritesheet creation
        spritepath = Path.cwd()/'Character'/'Character_UpRight.png'
        self.uprightframecount=0
        self.uprightframes=[]
        uprightsprite = SpriteSheet(str(spritepath))
        x=9
        for loop in range (4):
            frame=uprightsprite.get_image(x,7,15,20)
            x+=32
            self.uprightframes.append(frame)

        #right animation spritesheet creation
        spritepath = Path.cwd()/'Character'/'Character_Right.png'
        self.rightframecount=0
        self.rightframes=[]
        rightsprite = SpriteSheet(str(spritepath))
        x=10
        for loop in range (4):
            frame=rightsprite.get_image(x,7,14,19)
            x+=32
            self.rightframes.append(frame)
        
        #left animation spritesheet creation
        spritepath = Path.cwd()/'Character'/'Character_Left.png'
        self.leftframecount=0
        self.leftframes=[]
        leftsprite = SpriteSheet(str(spritepath))
        x=8
        for loop in range (4):
            frame=leftsprite.get_image(x,7,14,19)
            x+=32
            self.leftframes.append(frame)

    def down(self):
        self.timer+=1
        frame = pygame.transform.scale(self.downframes[self.downframecount],(60,75))
        if self.timer%5==0:
            screen.blit(frame,(self.characterposx,self.characterposy))
            self.downframecount+=1
        else:
            screen.blit(frame,(self.characterposx,self.characterposy))
        if self.characterposy!=625:
            self.characterposy+=5
        if self.downframecount==4:
            self.downframecount=0

    def downleft(self):
        self.timer+=1
        frame = pygame.transform.scale(self.downleftframes[self.downleftframecount],(60,75))
        if self.timer%5==0:
            screen.blit(frame,(self.characterposx,self.characterposy))
            self.downleftframecount+=1
        else:
            screen.blit(frame,(self.characterposx,self.characterposy))
        if self.characterposy!=625 and self.characterposx!=0:
            self.characterposy+=5
            self.characterposx-=5
        if self.downleftframecount==4:
            self.downleftframecount=0
    
    def downright(self):
        self.timer+=1
        frame = pygame.transform.scale(self.downrightframes[self.downrightframecount],(60,75))
        if self.timer%5==0:
            screen.blit(frame,(self.characterposx,self.characterposy))
            self.downrightframecount+=1
        else:
            screen.blit(frame,(self.characterposx,self.characterposy))
        if self.characterposy!=625 and self.characterposx!=840:
            self.characterposy+=5
            self.characterposx+=5
        if self.downrightframecount==4:
            self.downrightframecount=0

    def up(self):
        self.timer+=1
        frame = pygame.transform.scale(self.upframes[self.upframecount],(60,75))
        if self.timer%5==0:
            screen.blit(frame,(self.characterposx,self.characterposy))
            self.upframecount+=1
        else:
            screen.blit(frame,(self.characterposx,self.characterposy))
        if self.characterposy!=0:
            self.characterposy-=5
        if self.upframecount==4:
            self.upframecount=0

    def upleft(self):
        self.timer+=1
        frame = pygame.transform.scale(self.upleftframes[self.upleftframecount],(60,75))
        if self.timer%5==0:
            screen.blit(frame,(self.characterposx,self.characterposy))
            self.upleftframecount+=1
        else:
            screen.blit(frame,(self.characterposx,self.characterposy))
        if self.characterposy!=0 and self.characterposx!=0:
            self.characterposy-=5
            self.characterposx-=5
        if self.upleftframecount==4:
            self.upleftframecount=0
    
    def upright(self):
        self.timer+=1
        frame = pygame.transform.scale(self.uprightframes[self.uprightframecount],(60,75))
        if self.timer%5==0:
            screen.blit(frame,(self.characterposx,self.characterposy))
            self.uprightframecount+=1
        else:
            screen.blit(frame,(self.characterposx,self.characterposy))
        if self.characterposy!=0 and self.characterposx!=840:
            self.characterposy-=5
            self.characterposx+=5
        if self.uprightframecount==4:
            self.uprightframecount=0

    def right(self):
        self.timer+=1
        frame = pygame.transform.scale(self.rightframes[self.rightframecount],(60,65))
        if self.timer%5==0:
            screen.blit(frame,(self.characterposx,self.characterposy))
            self.rightframecount+=1
        else:
            screen.blit(frame,(self.characterposx,self.characterposy))
        if self.characterposx!=840:
            self.characterposx+=5
        if self.rightframecount==4:
            self.rightframecount=0
        
    def left(self):
        self.timer+=1
        frame = pygame.transform.scale(self.leftframes[self.leftframecount],(60,65))
        if self.timer%5==0:
            screen.blit(frame,(self.characterposx,self.characterposy))
            self.leftframecount+=1
        else:
            screen.blit(frame,(self.characterposx,self.characterposy))
        if self.characterposx!=0:
            self.characterposx-=5
        if self.leftframecount==4:
            self.leftframecount=0
    
    def getrect(self):
        self.rect=pygame.Rect(self.characterposx+5,self.characterposy+12,50,50)
        # pygame.draw.rect(screen,(0,0,0),self.rect) #shows hurtbox
        return self.rect

class fireball:
    #fireball animation and other stuff that needs to be preset
    def __init__(self):
        self.fireballframes = [(pygame.image.load(str(Path.cwd()/'Fireball'/'FB001.png'))),(pygame.image.load(str(Path.cwd()/'Fireball'/'FB002.png'))),(pygame.image.load(str(Path.cwd()/'Fireball'/'FB003.png'))),(pygame.image.load(str(Path.cwd()/'Fireball'/'FB004.png'))),(pygame.image.load(str(Path.cwd()/'Fireball'/'FB005.png')))]
        self.fireballcount=0
        self.timer =0

    #puts fireball randomly along the border of the screen
    #chooses a random position along the edge of the window and makes it the start pos for the fireball
    def startposition(self):
        start = random.choice(('x','y'))
        if start == 'x':
            self.startposx = random.choice((0,900))
            self.startposy = random.choice(range(900))
        else:
            self.startposy = random.choice ((0,700))
            self.startposx = random.choice((range(900)))

    #gets angle from start to person
    #directions fireball to player
    #i am trig god i am 100 in trig ez dub i live in radians i breath in radians i see in radians i am radians
    def getangle(self):
        self.run = False
        try:
            self.x = character.characterposx-self.startposx
            self.y = character.characterposy-self.startposy
            self.angle = math.atan((self.y/self.x))
            self.angle = math.degrees(self.angle)
        except ZeroDivisionError:
            self.angle = 0
        return self.angle

    #actually moves the fireball
    def cast(self):
        #animation of fireball
        self.timer+=1
        frame = pygame.transform.scale(self.fireballframes[self.fireballcount],(120,60))
        
        #orientation of fireball
        if self.x<0:
            frame = pygame.transform.flip(frame,True,False)

        frame = pygame.transform.rotate(frame, -self.angle)

        #actual animation of fireball
        if self.timer%10==0:
            screen.blit(frame,(self.startposx,self.startposy))
            self.fireballcount+=1
        else:
            screen.blit(frame,(self.startposx,self.startposy))
        if self.fireballcount == 5:
            self.fireballcount = 0
    
        #movement of fireball
        self.startposx += round(self.x/60)
        self.startposy += round(self.y/60)
    
    def getrect(self):
        self.rect = pygame.Rect(self.startposx+40,self.startposy+40,40,40)
        # pygame.draw.rect(screen,(0,0,0),self.rect) #shows hitbox
        return self.rect

#player instance
character = character()

#death frames
class death:
    def __init__(self):
        self.deathframes = [pygame.image.load(str(Path.cwd()/'Explosion'/'1.png')),pygame.image.load(str(Path.cwd()/'Explosion'/'2.png')),pygame.image.load(str(Path.cwd()/'Explosion'/'3.png')),pygame.image.load(str(Path.cwd()/'Explosion'/'4.png')),pygame.image.load(str(Path.cwd()/'Explosion'/'5.png')),pygame.image.load(str(Path.cwd()/'Explosion'/'6.png')),pygame.image.load(str(Path.cwd()/'Explosion'/'7.png')),pygame.image.load(str(Path.cwd()/'Explosion'/'8.png')),pygame.image.load(str(Path.cwd()/'Explosion'/'9.png')),pygame.image.load(str(Path.cwd()/'Explosion'/'10.png')),pygame.image.load(str(Path.cwd()/'Explosion'/'11.png')),pygame.image.load(str(Path.cwd()/'Explosion'/'12.png'))]
        self.timer=0
        self.deathframecount=0
        
    def die(self):
        self.timer+=1
        if self.timer%3==0:
            frame = self.deathframes[self.deathframecount]
            self.deathframecount+=1
        else:
            frame = self.deathframes[self.deathframecount]
 
        frame = pygame.transform.scale(frame,(150,150))
        screen.blit(bg,(0,0))
        screen.blit(frame,(character.characterposx-50,character.characterposy-50))    

death=death()

#background
bg=pygame.image.load(str(Path.cwd()/'bg'/'bg.jpg'))



#retry icon
respawnbutton = pygame.image.load(str(Path.cwd()/'icon'/'respawn.png'))
respawnrect = pygame.Rect(107,450,687,69)
respawnbuttondark= respawnbutton.copy()
respawnbuttondark.fill((100,100,100), special_flags=pygame.BLEND_RGBA_MIN)

#fireball intances
fireball1 = fireball()
fireball2 = fireball()
fireball3 = fireball()
fireball4 = fireball()
fireball5 = fireball()

#stuff that needs to be defined
run=True
retry = True 
fps = 60
dead = False
respawn = False
timer=0
clock=pygame.time.Clock()

#main loop
while run:
    clock.tick(fps)
    #variables that need to be defined beforehand
    #resets
    direction = 'down'
    down = False
    downleft = False
    up = False
    right = False
    left = False



    #resets fireball pos
    fireball1.startposition()
    fireball1.getangle()

    fireball2.startposition()
    fireball2.getangle()

    
    fireball3.startposition()
    fireball3.getangle()

    
    fireball4.startposition()
    fireball4.getangle()

    fireball5.startposition()
    fireball5.getangle()

    fireballlist = [fireball1,fireball2,fireball3,fireball4,fireball5]
    score = 0
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            run = False

    #game loop
    while retry:
        clock.tick(fps)
        screen.blit(bg,(0,0))

        #shows score
        scoretext=pygame.font.Font(str(Path.cwd()/'Font'/'pixel.ttf'),50).render(str(score),True,(255,255,255),True)
        scorelength = pygame.font.Font(str(Path.cwd()/'Font'/'pixel.ttf'),50).size(str(score))
        screen.blit(scoretext,((900-scorelength[0])/2,5))


        #go go go fireballs go vroom vroom skrrrrt skrrt
        fireball1.cast()
        if score>3:
            fireball2.cast()
        if score>15:
            fireball3.cast()
        if score>31:
            fireball4.cast()
        if score>51:
            fireball5.cast()
        
        #score that doesn't rly work yet
        for fireball in fireballlist:
            if fireball.startposx <0 or fireball.startposx >900:
                score += 1
                fireball.startposition()
                fireball.getangle()
            elif fireball.startposy<0 or fireball.startposy>700:
                score += 1
                fireball.startposition()
                fireball.getangle()

        #player and fireball collision
        for fireball in fireballlist:
            if pygame.Rect.colliderect(fireball.getrect(),character.getrect()) == 1:
                retry = False
                dead = True

        #event handling
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit
                retry = False
                run = False
                
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    direction = 'down'
                    down=True
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    direction = 'up'
                    up = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    direction = 'right'
                    right = True
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    direction = 'left'
                    left = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    down = False
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    left = False

        #character movement
        #idle frame
        if down == False and up == False and right == False and left == False:
            if direction == 'down':
                frame = pygame.transform.scale(character.downframes[0],(60,75))
                screen.blit(frame,(character.characterposx,character.characterposy))
            if direction == 'up':
                frame = pygame.transform.scale(character.upframes[0],(60,75))
                screen.blit(frame,(character.characterposx,character.characterposy))
            if direction == 'right':
                frame = pygame.transform.scale(character.rightframes[0],(60,65)) 
                screen.blit(frame,(character.characterposx,character.characterposy))
            if direction == 'left':
                frame = pygame.transform.scale(character.leftframes[0],(60,65)) 
                screen.blit(frame,(character.characterposx,character.characterposy))
            if direction == 'downleft':
                frame = pygame.transform.scale(character.downleftframes[0],(60,75)) 
                screen.blit(frame,(character.characterposx,character.characterposy))
            if direction == 'downright':
                frame = pygame.transform.scale(character.downrightframes[0],(60,75))
                screen.blit(frame,(character.characterposx,character.characterposy))
            if direction == 'upleft':
                frame = pygame.transform.scale(character.upleftframes[0],(60,75))
                screen.blit(frame,(character.characterposx,character.characterposy))
            if direction == 'upright':
                frame = pygame.transform.scale(character.uprightframes[0],(60,75))
                screen.blit(frame,(character.characterposx,character.characterposy))

    #actual movement
        elif down==True and left == True:
            direction = 'downleft'
            character.downleft()
        elif down==True and right == True:
            direction = 'downright'
            character.downright()
        elif up == True and left == True:
            direction = 'upleft'
            character.upleft()
        elif up == True and right == True:
            direction = 'upright'
            character.upright()
        elif down:
            character.down()
        elif up:
            character.up()
        elif right:
            character.right()
        elif left:
            character.left()

        pygame.display.update()
    
    #death animation
    if dead:
        death.die()
        if death.deathframecount==11:
            screen.blit(bg,(0,0))
            dead=False
            death.deathframecount=0
            screen.blit(respawnbutton,(107,450))
            respawn = True
        pygame.display.update()

    #fuck this shit looks ugly smh
    #im too lazy to make that more variables
    if respawn:
        if respawnrect.collidepoint(pygame.mouse.get_pos())==1:
            screen.blit(bg,(0,0))
            youdiedlength = pygame.font.Font(str(Path.cwd()/'Font'/'pixel.ttf'),50).size('You Died!')
            screen.blit(scoretext,((900-scorelength[0])/2,(250)))
            youdied = pygame.font.Font(str(Path.cwd()/'Font'/'pixel.ttf'),50).render('You Died!',True,(255,255,255))
            screen.blit(youdied,((920-youdiedlength[0])/2,100))
            screen.blit(respawnbuttondark,(107,450))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    respawn = False
                    retry = True
                    character.characterposx=425
                    character.characterposy=300
                    
        else:
            screen.blit(bg,(0,0))
            scorelength = pygame.font.Font(str(Path.cwd()/'Font'/'pixel.ttf'),50).size(str(score))
            youdiedlength = pygame.font.Font(str(Path.cwd()/'Font'/'pixel.ttf'),50).size('You Died!')
            screen.blit(scoretext,((900-scorelength[0])/2,(250)))
            youdied = pygame.font.Font(str(Path.cwd()/'Font'/'pixel.ttf'),50).render('You Died!',True,(255,255,255))
            screen.blit(youdied,((920-youdiedlength[0])/2,100))
            screen.blit(respawnbutton,(107,450))

        pygame.display.update()
    