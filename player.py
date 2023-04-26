import pygame
from settings import *
import image

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 
dir_ = 'ếch/' #gán tệp hình ảnh
animation_ = [] # tạo một list 

for i in range(1,12): #ảnh chạy lần lượt từ ảnh 1-ảnh 11
    actor = pygame.image.load(dir_ + str(i) + '.png') 
    animation_.append(actor) #đưa biến actor vào list animation

class Player():
    def __init__(self):
        self.x = 100
        self.y = 250
        self.animation_ = animation_
        self.img = animation_[0]
        self.frame = 0
        self.time_int = pygame.time.get_ticks()
        self.orig_image = image.load("ếch/1.png", size=(HAND_SIZE, HAND_SIZE))
        self.image = self.orig_image.copy()
        
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1])
        self.left_click = False

    def draw(self, surface):
        
        DISPLAYSURF.blit(surface, (self.x, self.y))

    def update_animation(self):
        self.time_now = pygame.time.get_ticks()
        cooldown = 100
        if self.time_now - self.time_int > cooldown:
            self.frame += 1
            if self.frame >= len(self.animation_):
                self.frame = 0
        self.img = self.animation_[self.frame]