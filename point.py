
import pygame
from settings import *
from random  import randint

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
        self.speed = 3
        self.numPoint=randint(0,2) 
        self.img = DRL #hình ảnh từ danh sách DRL
    def draw(self):
        DISPLAYSURF.blit(self.img[self.numPoint], (int(self.x), int(self.y)))
    def update(self): #cập nhật vị trí của đrl
        self.x -= self.speed 
        if self.x < -200: 
            self.numPoint=randint(0,2) 
            self.x = randint(200,900) 
            self.y = randint(0,500)
def drawScore(score): # hiện điểm
    value = score_font.render("Your score: " + str(score), True, (255, 255, 102))
    DISPLAYSURF.blit(value, [0, 0]) #hiển thị vb lên bề mặt
def drawTime(time): # thời gian còn lại, time là đầu vào, dùng score_font
    value = score_font.render("Time remaining: "+str(time), True, (255, 100, 102))
    DISPLAYSURF.blit(value, [500, 50])