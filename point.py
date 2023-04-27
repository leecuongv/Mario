
import pygame
from settings import *
from random  import randint
from settings import *

import time

clock = pygame.time.Clock()

DRL =[] #tạo ds trống
#thêm 3 hình ảnh vào ds DRL
a=DRL.append(pygame.image.load('5.png'))
b=DRL.append(pygame.image.load('10.png'))
c=DRL.append(pygame.image.load('20.png'))

font_style = pygame.font.SysFont("bahnschrift", 50)
score_font = pygame.font.SysFont("comicsansms", 35)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #tạo cửa sổ với kích thước
class Point():
    def __init__(self):
        self.x = 200
        self.y = 300
        self.speed = 100
        self.numPoint=randint(0,2) 
        self.img = DRL #hình ảnh từ danh sách DRL
        self.current_frame = 0
        self.animation_timer = 0
        
        
    def draw(self):
        self.animate()
        DISPLAYSURF.blit(self.img[self.numPoint], (int(self.x), int(self.y)))
        
    def update(self): #cập nhật vị trí của đrl
        self.x -= self.speed 
        if self.x < -200: 
            self.numPoint=randint(0,2) 
            self.x = randint(200,900) 
            self.y = randint(0,500)
    
    def animate(self): # change the frame of the insect when needed
        t = time.time()
        if t > self.animation_timer:
            self.animation_timer = t + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.img)-1:
                self.current_frame = 0