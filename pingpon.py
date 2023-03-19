from pygame import*

class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x,player_y, player_speed, wight, height):
        super().__init__()
        

        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speedself.rect = self.image.get.rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(seslf.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
back1 = 'фоновая-сцена-зоопарка-с-знаками-и-следами-изображением-знака-трека-162850781.jpg'
background = transform.scale(image.load(back1),(win_width, win_height))

game = True
finish = False
FPS = 144
racket1 = Player('16328137282623s.jpg', 30, 200, 4, 50, 150)
racket2 = Player('16328137282623s.jpg', 520, 200, 4, 50, 150) 
ball = GameSprite('620ea84ce3702bc204da3f512eb01461.png', 200, 200, 2, 50, 50)
font.init()
font = font.SysFont('consolas', 35)
lose1 = font.render('PLAYER 1 LOSE!', True,(180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True,(180, 0, 0))
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window_blit(background, (0, 0))
        racket1.update_l()
