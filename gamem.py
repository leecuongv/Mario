import pygame
import time
import random
from settings import *
from background import Background
from player import Player
import cv2
import ui
from random  import randint
import keyboard
from point import Point
mypoint = Point()
class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()


    def reset(self): # reset all the needed variables
        
        self.player = Player()
        
        self.score = 0
        self.game_start_time = time.time()
        
        self.x_coor=0 
        self.y_coor=200


    def draw(self):
        # draw the background
        self.background.draw(self.surface)
        self.player.draw()
        # draw the score
        ui.draw_text(self.surface, f"Score : {self.score}", (300, 5), COLORS["score"], font=FONTS["medium"],
                    shadow=False, shadow_color=(255,255,255))
        # draw the time left
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] # change the text color if less than 5 s left
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (SCREEN_WIDTH//2 + 200, 5),  timer_text_color, font=FONTS["medium"],
                    shadow=False, shadow_color=(255,255,255))


    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)


    def update(self):
        
        #self.load_camera()
        self.game_time_update()
        global mypoint
        self.draw()

        if self.time_left > 0:
            
            if keyboard.is_pressed("right"):
                self.x_coor+=10 # nút phải => x tăng 10
                print(self.x_coor)
            if keyboard.is_pressed("left"):
                self.x_coor-=10 # trái => x giảm 10
                print(self.x_coor)
            if keyboard.is_pressed("up"):
                self.y_coor-=10 # lên=> y giảm 10
                print(self.y_coor)
            if keyboard.is_pressed("down"):
                self.y_coor+=10 # xuống => y tăng 10
                print(self.y_coor)
        
            self.player.x=self.x_coor
            self.player.y=self.y_coor
            self.player.draw()
            self.player.update_animation()
            #vẽ và update đrl:
           
            
            #cập nhật đối tượng người chơi và đrl, đồng thời hiển thị điểm hiện tại và thời gian còn lại:
            if (abs(self.player.x-mypoint.x)<=50 and abs(self.player.y- mypoint.y)<=50): #tạo va chạm
                if (mypoint.numPoint==0): 
                    self.score+=5
                elif (mypoint.numPoint==1):
                    self.score+=10
                else:
                    self.score+=20
                mypoint.x=randint(200,900)
                mypoint.y=randint(0,500)  
                mypoint.numPoint=randint(0,2) 
                mypoint.draw() #in ra đrl
                mypoint.update() # cập nhật đrl

        else: # when the game is over
            if ui.button(self.surface, 540, "Continue"):
                return "menu"


