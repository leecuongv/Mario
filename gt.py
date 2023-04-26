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

pygame.mixer.music.load('nhac.mp3') #tải nhạc
pygame.mixer.music.play(-1) # -1 là đối số, chỉ định nhạc lặp vô thời hạn cho đến khi ctr kết thúc

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) #tạo cửa sổ với kích thước
pygame.display.set_caption('FLY FROG GAME') #đặt tên tiêu đề

#tạo font, kích thước cho đối tượng:
font_style = pygame.font.SysFont("bahnschrift", 50)
score_font = pygame.font.SysFont("comicsansms", 35)
finalScoreFont = pygame.font.SysFont('Bradley Hand ITC', 50, bold = pygame.font.Font.bold) 


class Background(): 
    def __init__(self): 
        self.x = 0 
        self.y = 0 
        self.speed = 3 #tốc độ
        self.img = BG 
        self.width = self.img.get_width() 
        self.height = self.img.get_height() 
    def draw(self): #vẽ hình nền lên bề mặt hiển thị
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        DISPLAYSURF.blit(self.img, (int(self.x + self.width), int(self.y)))
    def update(self): #sử dụng hàm update để tạo background cuộn vô hạn
        self.x -= self.speed 
        if self.x < -self.width: 
            self.x += self.width

dir_ = 'ếch/' #gán tệp hình ảnh
animation_ = [] # tạo một list 
for i in range(1,12): #ảnh chạy lần lượt từ ảnh 1-ảnh 11
    actor = pygame.image.load(dir_ + str(i) + '.png') 
    animation_.append(actor) #đưa biến actor vào list animation

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
        if self.time_now - self.time_int > cooldown: #xét nếu thời gian
            self.frame += 1 
            if self.frame >= len(self.animation_):
                self.frame = 0
        self.img = self.animation_[self.frame] #update hình ảnh

DRL =[] #tạo ds trống
#thêm 3 hình ảnh vào ds DRL
a=DRL.append(pygame.image.load('5.png'))
b=DRL.append(pygame.image.load('10.png'))
c=DRL.append(pygame.image.load('20.png'))

#phần kết thúc game
class Button: 
    def __init__(self, x, y, width, height, color, text='', font_size=32, font_color=(255, 255, 255), hover_color=None, corner_radius=20):
        self.rect = pygame.Rect(x, y, width, height) # x,y là tọa độ nút; w,h là kích thước nút
        self.color = color 
        self.text = text 
        self.font_size = font_size 
        self.font_color = font_color 
        self.font = score_font 
        self.hover_color = hover_color if hover_color is not None else self.color
        self.corner_radius = corner_radius 
        
    def draw(self, screen): #vẽ nút lên màn hình
        mouse_pos = pygame.mouse.get_pos() #vị trí chuột hiện tại 
        if self.rect.collidepoint(mouse_pos): #kiểm tra xem chuột có nằm trên nút k:
            color = self.hover_color 
        else: #nếu không thì giữ nguyên màu nút
            color = self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=self.corner_radius)
        if self.text != '': 
            text = self.font.render(self.text, True, self.font_color) #hiển thị văn bản với font, màu chữ chỉ định trong nút
            text_rect = text.get_rect(center=self.rect.center) #hiển thị văn bản tại vị trí trung tâm trong HCN = thuộc tính get_rect và center
            screen.blit(text, text_rect) #vẽ ra trên màn hình
            
    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False

#tạo đối tượng cho phần điểm rèn luyện:
class point():
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

def main(): #khởi tạo các đối tượng
    bg = Background() # hình nền
    pl = Player() #nhân vật 
    mypoint=point() #đrl
    x_coor=0 
    y_coor=200 
    totalScore=0 #khởi tạo điểm ban đầu
    drawScore(totalScore) #hiển thị điểm ban đầu

    close_button = Button(470, 350, 150, 50, "gray", 'Close', corner_radius=15,hover_color="red")
     #vị trí: x,y,weight, heigh, màu nền:xanh lục, vb:try again, màu khi rê chuột: xanh lá
    try_again_button = Button(670, 350, 200, 50,color=(0,204,102) , text='Try Again',hover_color="green")

    timeCount = pygame.time.get_ticks() #khởi tạo thời gian 
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
        if pygame.time.get_ticks()-timeCount<60000:
            drawTime(int(pygame.time.get_ticks()-timeCount)) 
            bg.draw() #hiện thị background
            bg.update() # update background

            #kiểm tra đầu vào bàn phím:
            if keyboard.is_pressed("right"):
                x_coor+=10 # nút phải => x tăng 10
            if keyboard.is_pressed("left"):
                x_coor-=10 # trái => x giảm 10
            if keyboard.is_pressed("up"):
                y_coor-=10 # lên=> y giảm 10
            if keyboard.is_pressed("down"):
                y_coor+=10 # xuống => y tăng 10
        
            pl.x=x_coor
            pl.y=y_coor
            pl.draw()
            pl.update_animation()
            #vẽ và update đrl:
            mypoint.draw()
            mypoint.update()
            drawScore(totalScore) #hiển thị điểm hiện tại

            drawTime(int(60-(pygame.time.get_ticks()-timeCount)/1000)) 
            
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
            pygame.display.update() 
            fpsClock.tick(FPS) #kiểm soát tốc độ khung hình trò chơi
        else: 
            bg.draw()
            bg.update()
            #hiển thị các cập nhật khi end game:
            value = font_style.render("TIME'S UP!!!!!", True, (255, 0, 0)) #hiển thị hết giờ
            DISPLAYSURF.blit(value, [550, 170]) #in ra với tọa độ x,y
            #kết quả điểm cuối với font, điểm hiện tại,màu sắc dòng chữ
            value = finalScoreFont.render(f"Your score: {totalScore}", True, (255, 128, 0)) 
            DISPLAYSURF.blit(value, [510, 250]) # in ra màn hình với tọa độ x,y
            
            close_button.draw(DISPLAYSURF) 
            try_again_button.draw(DISPLAYSURF)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.is_clicked(pygame.mouse.get_pos()): #nếu ng chơi nhân nút close:
                    pygame.quit() 
                    sys.exit() 
                if try_again_button.is_clicked(pygame.mouse.get_pos()): #nhấn nút try again
                    timeCount = pygame.time.get_ticks() 
                    totalScore=0 
            pygame.display.update() #cập nhật các thay đổi
            fpsClock.tick(FPS)  #kiểm soát tốc độ khung hình

if __name__ == '__main__':
    main() 
