from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 5:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 5:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0

speed = 5
rocket1 = Player('51539.png', 50, 0, 30, 100, speed)
rocket2 = Player('51539.png', 620, 0, 30, 100, speed)
back = ((160, 255, 255))
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping pong')
window.fill(back)
run = True
finish = False
clock = time.Clock()
FPS = 60
rocket1.update_l()
rocket2.update_r()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        rocket1.update_l()
        rocket2.update_r()
        rocket1.reset()
        rocket2.reset()
        
    display.update()
    clock.tick(FPS)
