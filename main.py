import pygame, sys
from pygame.locals import *
from random  import randint
import keyboard 
pygame.init()

FPS = 15  
fpsClock = pygame.time.Clock()

WINDOWWIDTH = 1350
WINDOWHEIGHT = 690

BG = pygame.image.load('sky.png')
BG = pygame.transform.scale(BG, (1350,690))

pygame.mixer.music.load('nhac.mp3')
pygame.mixer.music.play(-1)

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('FLY FROG GAME')
font_style = pygame.font.SysFont("bahnschrift", 50)
score_font = pygame.font.SysFont("comicsansms", 35)
finalScoreFont = pygame.font.SysFont('Bradley Hand ITC', 50, bold = pygame.font.Font.bold)

class Background():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 3
        self.img = BG
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    def draw(self):
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        DISPLAYSURF.blit(self.img, (int(self.x + self.width), int(self.y)))
    def update(self):
        self.x -= self.speed 
        if self.x < -self.width:
            self.x += self.width

dir_ = 'ếch/' 
animation_ = []
for i in range(1,12):
    actor = pygame.image.load(dir_ + str(i) + '.png')
    animation_.append(actor)

class Player():
    def __init__(self):
        self.x=100
        self.y=250
        self.animation_ = animation_
        self.img= animation_[0]
        self.frame = 0
        self.time_int = pygame.time.get_ticks()
    def draw(self):
        self.update_animation()
        DISPLAYSURF.blit(self.img,(self.x,self.y))
    def update_animation(self): 
        self.time_now = pygame.time.get_ticks()
        cooldown = 100
        if self.time_now - self.time_int > cooldown:
            self.frame += 1
            if self.frame >= len(self.animation_):
                self.frame = 0
        self.img = self.animation_[self.frame]

DRL =[]
a=DRL.append(pygame.image.load('5.png'))
b=DRL.append(pygame.image.load('10.png'))
c=DRL.append(pygame.image.load('20.png'))

class Button:
    def __init__(self, x, y, width, height, color, text='', font_size=32, font_color=(255, 255, 255), hover_color=None, corner_radius=20):
        self.rect = pygame.Rect(x, y, width, height) 
        self.color = color
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.font = score_font
        self.hover_color = hover_color if hover_color is not None else self.color
        self.corner_radius = corner_radius
        
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            color = self.hover_color
        else:
            color = self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=self.corner_radius)
        if self.text != '':
            text = self.font.render(self.text, True, self.font_color)
            text_rect = text.get_rect(center=self.rect.center)
            screen.blit(text, text_rect)
            
    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False

class point():
    def __init__(self):
        self.x = 200
        self.y = 300
        self.speed = 3
        self.numPoint=randint(0,2)
        self.img = DRL
    def draw(self):
        DISPLAYSURF.blit(self.img[self.numPoint], (int(self.x), int(self.y)))
    def update(self):
        self.x -= self.speed
        if self.x < -200:
            self.numPoint=randint(0,2)
            self.x = randint(200,900)
            self.y = randint(0,500)

def drawScore(score): 
    value = score_font.render("Your score: " + str(score), True, (255, 255, 102))
    DISPLAYSURF.blit(value, [0, 0])
def drawTime(time):
    value = score_font.render("Time remaining: "+str(time), True, (255, 100, 102))
    DISPLAYSURF.blit(value, [500, 50])


def main():
    bg = Background()
    pl = Player()
    mypoint=point()
    x_coor=0 
    y_coor=200
    totalScore=0
    drawScore(totalScore)
    close_button = Button(470, 350, 150, 50, "gray", 'Close', corner_radius=15,hover_color="red")
    try_again_button = Button(670, 350, 200, 50,color=(0,204,102) , text='Try Again',hover_color="green")

    timeCount = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if pygame.time.get_ticks()-timeCount<60000:
            drawTime(int(pygame.time.get_ticks()-timeCount))
            bg.draw()
            bg.update()
            if keyboard.is_pressed("right"):
                x_coor+=10
            if keyboard.is_pressed("left"):
                x_coor-=10
            if keyboard.is_pressed("up"):
                y_coor-=10
            if keyboard.is_pressed("down"):
                y_coor+=10
            pl.x=x_coor 
            pl.y=y_coor
            pl.draw()
            pl.update_animation()
            mypoint.draw()
            mypoint.update()
            drawScore(totalScore)
            drawTime(int(60-(pygame.time.get_ticks()-timeCount)/1000))
            if (abs(pl.x-mypoint.x)<=50 and abs(pl.y-mypoint.y)<=50):
                if (mypoint.numPoint==0):
                    totalScore+=5
                elif (mypoint.numPoint==1):
                    totalScore+=10
                else:
                    totalScore+=20
                mypoint.x=randint(200,900)
                mypoint.y=randint(0,500)
                mypoint.numPoint=randint(0,2)
                mypoint.draw()
                mypoint.update()
            pygame.display.update()
            fpsClock.tick(FPS)
        else:
            bg.draw()
            bg.update()
            
            value = font_style.render("TIME'S UP!!!!!", True, (255, 0, 0))
            DISPLAYSURF.blit(value, [550, 170])

            value = finalScoreFont.render(f"Your score: {totalScore}", True, (255, 128, 0))
            DISPLAYSURF.blit(value, [510, 250])

            close_button.draw(DISPLAYSURF)
            try_again_button.draw(DISPLAYSURF)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.is_clicked(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                if try_again_button.is_clicked(pygame.mouse.get_pos()):
                    timeCount = pygame.time.get_ticks()
                    totalScore=0
            pygame.display.update()
            fpsClock.tick(FPS)
if __name__ == '__main__':
    main()