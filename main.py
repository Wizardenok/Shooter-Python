import datetime
from random import randint
from pygame import *

init()
window = display.set_mode((700, 500))
clock = time.Clock()
display.set_caption('Догонялки')
background = (
    transform.scale(
        image.load('galaxy.jpg'),
        (700, 500)))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= -100:
            self.kill()


class Player(GameSprite):
    def __init__(self, player_image, bullet_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.bullet = bullet_image

    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= 10
        if keys_pressed[K_d] and self.rect.x < 635:
            self.rect.x += 10

    def fire(self):
        bullet = Bullet(self.bullet, self.rect.x, self.rect.y, 5)
        bullets.add(bullet)


class HP:
    def __init__(self, hp_w, hp_h, hp_rocket):
        self.hp_w = hp_w
        self.hp_h = hp_h
        self.hp_rocket = hp_rocket

    def update(self, rocket_x, rocket_y):
        self.health_bar_filled = int(self.hp_rocket / 100 * self.hp_w)
        self.health_bar_rect = Rect(rocket_x + 30 - self.hp_w // 2, rocket_y + 70, self.health_bar_filled, self.hp_h)
        self.health_bar_outline_rect = Rect(rocket_x + 30 - self.hp_w // 2, rocket_y + 70, self.hp_w, self.hp_h)

    def draw(self):
        draw.rect(window, (255, 0, 0), self.health_bar_rect)
        draw.rect(window, (255, 255, 255), self.health_bar_outline_rect, 2)

    def get_hp(self, hp_rocket):
        if hp_rocket < 0:
            self.hp_rocket = 0
        else:
            self.hp_rocket = hp_rocket


class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, flag):
        super().__init__(player_image, player_speed, player_y, player_x)
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.flag = flag

    def update(self):
        if (self.rect.y >= 0 and self.rect.y <= 500) and self.flag == 1:
            self.rect.y += self.speed
        if self.rect.y >= 500 and self.flag == 1:
            self.rect.y = 0
            self.rect.x = randint(0, 625)
            self.speed = randint(1, 2)
        if (self.rect.y >= 0 and self.rect.y <= 500) and self.flag == 2:
            self.rect.y += self.speed
        if self.rect.y >= 500 and self.flag == 2:
            self.rect.y = 0
            self.speed = randint(1, 2)
            self.rect.x = randint(0, 625)
        if (self.rect.y >= 0 and self.rect.y <= 500) and self.flag == 3:
            self.rect.y += self.speed
        if self.rect.y >= 500 and self.flag == 3:
            self.rect.y = 0
            self.speed = randint(1, 2)
            self.rect.x = randint(0, 625)
        if (self.rect.y >= 0 and self.rect.y <= 500) and self.flag == 4:
            self.rect.y += self.speed
        if self.rect.y >= 500 and self.flag == 4:
            self.rect.y = 0
            self.speed = randint(1, 2)
            self.rect.x = randint(0, 625)
        if (self.rect.y >= 0 and self.rect.y <= 500) and self.flag == 5:
            self.rect.y += self.speed
        if self.rect.y >= 500 and self.flag == 5:
            self.rect.y = 0
            self.speed = randint(1, 2)
            self.rect.x = randint(0, 625)
        if (self.rect.y >= 0 and self.rect.y <= 500) and self.flag == 6:
            self.rect.y += self.speed
        if self.rect.y >= 500 and self.flag == 6:
            self.rect.y = 0
            self.speed = randint(1, 2)
            self.rect.x = randint(0, 625)
        if (self.rect.y >= 0 and self.rect.y <= 500) and self.flag == 7:
            self.rect.y += self.speed
        if self.rect.y >= 500 and self.flag == 7:
            self.rect.y = 0
            self.speed = randint(1, 2)
            self.rect.x = randint(0, 625)
        if (self.rect.y >= 0 and self.rect.y <= 500) and self.flag == 8:
            self.rect.y += self.speed
        if self.rect.y >= 500 and self.flag == 8:
            self.rect.y = 0
            self.speed = randint(1, 2)
            self.rect.x = randint(0, 625)
        if (self.rect.y >= 0 and self.rect.y <= 500) and self.flag == 9:
            self.rect.y += self.speed
        if self.rect.y >= 500 and self.flag == 9:
            self.rect.y = 0
            self.speed = randint(1, 2)
            self.rect.x = randint(0, 625)
        if (self.rect.y >= 0 and self.rect.y <= 500) and self.flag == 10:
            self.rect.y += self.speed
        if self.rect.y >= 500 and self.flag == 10:
            self.rect.y = 0
            self.speed = randint(1, 2)
            self.rect.x = randint(0, 625)


class Ufo(GameSprite):
    def __init__(self, enemy_image, player_x, player_y, player_speed):
        super().__init__(enemy_image, player_speed, player_y, player_x)

    def update(self):
        pass


def get_font(killed_enemies, size, font_for_text, rgb):
    font_for_text = font.Font(font_for_text, size)
    text_killed_enemies = font_for_text.render(str(killed_enemies), True, rgb)
    window.blit(text_killed_enemies, (0, 0))


player = Player('rocket.png', 'bullet.png', 100, 410, 3)
enemies = []
for i in range(10):
    enemies.append(Enemy('asteroid.png', randint(0, 625), 0, randint(1, 2), i + 1))
ufos = list()
ufos.append(Ufo('ufo.png', 0, 0, 2))

count_killed_enemies = 0
bullets = sprite.Group()
LastShotTime = datetime.datetime.now()
fire_sound = mixer.Sound('fire.ogg')
fire_sound.set_volume(0.03)
background_music = open('space.ogg')
mixer.music.load(background_music)
mixer.music.set_volume(0.05)
mixer.music.play()
hp_rocket = 100
hp_bar = HP(50, 10, hp_rocket)

game = True
player_killed = False
while game:
    window.blit(background, (0, 0))
    if player_killed == False:
        current_time = datetime.datetime.now()
        keys = key.get_pressed()
        get_font(count_killed_enemies, 36, None, (102, 0, 255))
        player.reset()
        player.update()
        hp_bar.update(player.rect.x, player.rect.y)  # Обновление позиции полосы жизни
        hp_bar.draw()  # Отрисовка полосы жизни


        # Update and draw bullets
        bullets.update()
        bullets.draw(window)

        for u in ufos:
            if count_killed_enemies % 10 == 0 and count_killed_enemies != 0:
                u.reset()
                u.update()

        for e in enemies:
            e.reset()
            e.update()
            for b in bullets:
                if sprite.collide_rect(b, e):
                    e.rect.y = 1000
                    b.kill()  # Удалить пулю при столкновении
                    count_killed_enemies = int(count_killed_enemies) + 1
            if sprite.collide_rect(player, e):
                e.rect.y = 1000
                hp_rocket -= 10 # Уменьшить HP ракеты на 10
                hp_bar.get_hp(hp_rocket)

        if hp_rocket <= 0:
            player_killed = True

        if keys[K_SPACE]:
            current_time = datetime.datetime.now()
            total_time = current_time - LastShotTime
            total_time = total_time.total_seconds()
            if total_time >= 0.5:
                player.fire()
                fire_sound.play()
                LastShotTime = current_time

     # if 1:
     # black_square = Rect((100, 100), (500, 300))
     # draw.rect(window, (0, 0, 0), black_square)

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)
