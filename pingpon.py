from pygame import*

class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x,player_y, player_speed, wight, height):
        super().__init__()
        

        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
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
clock = time.Clock()
FPS = 60
racket1 = Player('16328137282623s.jpg', 30, 200, 4, 50, 150)
racket2 = Player('16328137282623s.jpg', 520, 200, 4, 50, 150) 
ball = GameSprite('620ea84ce3702bc204da3f512eb01461.png', 200, 200, 2, 50, 50)
font.init()
font = font.SysFont('consolas', 35)
lose1 = font.render('PLAYER 1 LOSE!', True,(180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True,(180, 0, 0))
speed_x = 3
speed_y = 3


score1 = 0
score2 = 0






while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        racket1.reset()
        racket2.reset()
        if sprite.collide_rect(racket1, ball):
            speed_x *= -1
            speed_y *= 1
            score1 = score1 + 1
        if sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
            score2 = score2 + 1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        text = font.render('Kilkict otbitux', 1, (0, 0, 255))
        window.blit(text, (130, 20))
        text_lose = font.render(str(score1) + " : " + str(score2), 1, (0, 0, 255))
        window.blit(text_lose, (250, 60))
        ball.reset()
        display.update()
    
    else:
        finisah = False
        score2 = 0
        score1 = 0
        time.delay(3000)
        ball = GameSprite('620ea84ce3702bc204da3f512eb01461.png',200, 200, 4, 50, 50)
    clock.tick(FPS)