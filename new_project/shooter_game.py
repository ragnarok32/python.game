from pygame import*
from time import time as time_count
from random import randint as rand

init()

mixer.init()
window = display.set_mode((600,600))
display.set_caption("runers")
background = transform.scale(
    image.load("background.jpg"),
    (600,600)
)
window.blit(background, (0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,  player_x, pleyer_y, size, player_speed):
        super().__init__()
        self.image = transform.scale(
            image.load(player_image),
            size
        )
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = pleyer_y
        self.speed = player_speed

    def draw_sprite (self):
        window.blit(self.image, (self.rect.x, self.rect.y))
shot_time = time_count()
class pleyer(GameSprite):
    def update(self, bullets):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if pressed_keys[K_d] and self.rect.x <= 535:
            self.rect.x += self.speed
        if pressed_keys[K_SPACE]:
            global shot_time
            if time_count() - shot_time >= 1:

                new_bullet = Bullet("bullet.png", self.rect.x + 30, self.rect.y, (10, 20), 5)
                bullets.add(new_bullet)       
                shot_time = time_count()

class Enemy(GameSprite):
    def update(self):
        global lose_score
        self.rect.y += self.speed
        self.draw_sprite()
        if self.rect.y > 600:
            self.kill()
            lose_score -= 1
    def is_touch(self, sprite_object):
        return self.rect.colliderect(sprite_object.rect)
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        self.draw_sprite()
def draw_label(score, text,text1, x, y):
    image = font.SysFont("Arial", 25).render(text + str(score) + text1, True, (100,12,101))
    window.blit(image, (x, y))

def draw_hearts(score):
    heart = transform.scale(
    image.load("live.png"),
    (20,20))
    x = 20
    for i in range(score):
        window.blit(heart, (x, 60))
        x += 25

first_corx = 100
first_cory = 520

pleyer1 = pleyer("rocket.png", first_corx, first_cory ,(70 ,50), 5)
pleyer1.draw_sprite()

clock = time.Clock()
game = True
bullets = sprite.Group()
wait = 0
times = 0
counter = 1
score = 0
lose_score = 3
enemies = sprite.Group()
len(enemies.sprites())
while game:

    window.blit(background, (0,0))

    if len(enemies.sprites()) < 5:
        xcor = rand(10 ,550)
        enemies.add(Enemy("ufo.png" , xcor , 8 ,( 80 , 50 ) , 1))

    pleyer1.draw_sprite()
    pleyer1.update(bullets)
    enemies.update()
    bullets.update()
    draw_hearts(lose_score)
    enemies_amount = len(enemies.sprites())
    sprite.groupcollide(bullets, enemies, True, True)
    if len(enemies.sprites()) < enemies_amount:
        score += enemies_amount - len(enemies.sprites())
    if wait == 60:
        times += 1
        wait = 0
    else:
        wait += 1
    draw_label(score, "Enemy killed:","", 0, 30)
    draw_label(times, "Time pleyed:","", 0, 0)
    if lose_score <= 0:
        break
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0)) 
    draw_label(score, "Enemy killed:","", 180, 210)
    draw_label(times, "you lose in:"," seconds", 180, 180)
    display.update()
    clock.tick(60)