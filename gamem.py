import pygame
import time
import random
from settings import *
from background import Background
from player import Player
import cv2
import ui

import keyboard

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()


    def reset(self): # reset all the needed variables
        self.insects = []
        self.player = Player()
        self.insects_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()


    def draw(self):
        # draw the background
        self.background.draw(self.surface)
        # draw the insects
        for insect in self.insects:
            insect.draw(self.surface)
        # draw the hand
        self.player.draw(self.surface)
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

        self.draw()

        if self.time_left > 0:
            
            if keyboard.is_pressed("right"):
                x_coor+=10 # nút phải => x tăng 10
            if keyboard.is_pressed("left"):
                x_coor-=10 # trái => x giảm 10
            if keyboard.is_pressed("up"):
                y_coor-=10 # lên=> y giảm 10
            if keyboard.is_pressed("down"):
                y_coor+=10 # xuống => y tăng 10
        
            self.player.x=x_coor
            self.player.y=y_coor
            self.player.draw()
            self.player.update_animation()
            #vẽ và update đrl:
           
            
            #cập nhật đối tượng người chơi và đrl, đồng thời hiển thị điểm hiện tại và thời gian còn lại:
            if (abs(pl.x-mypoint.x)<=50 and abs(pl.y-mypoint.y)<=50): #tạo va chạm
                if (mypoint.numPoint==0): 
                    totalScore+=5
                elif (mypoint.numPoint==1):
                    totalScore+=10
                else:
                    totalScore+=20
                mypoint.x=randint(200,900)
                mypoint.y=randint(0,500)  
                mypoint.numPoint=randint(0,2) 
                mypoint.draw() #in ra đrl
                mypoint.update() # cập nhật đrl

        else: # when the game is over
            if ui.button(self.surface, 540, "Continue", click_sound=self.sounds["slap"]):
                return "menu"


        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
