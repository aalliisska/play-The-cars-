import os
import pygame
import random
import sys


class EnemyBad(pygame.sprite.Sprite):
    def __init__(self, sx, sy):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemybad_img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black)
        self.rect.x = random.randrange(0, w)
        self.rect.y = random.randrange(-50, 0)
        self.sx = sx
        self.sy = sy
        self.speedy = random.randrange(self.sy, self.sy + 2)
        self.speedx = random.randrange(-2, 2)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > h + 15 or self.rect.left < -25 or self.rect.right > w + 20:
            self.rect.x = random.randrange(0, w)
            self.rect.y = random.randrange(-50, 0)
            self.speedy = random.randrange(3, 4)

    def newenemys(self, x, sx, sy):
        for i in range(x):
            enemybad = EnemyBad(sx, sy)
            all_sprites.add(enemybad)
            enemysbad.add(enemybad)


class EnemyBadRed(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemybadred_img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black)
        self.rect.x = random.randrange(0, w)
        self.rect.y = random.randrange(-50, 0)
        self.speedy = random.randrange(2, 5)
        self.speedx = random.randrange(-2, 2)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > h + 15 or self.rect.left < -25 or self.rect.right > w + 20:
            self.rect.x = random.randrange(0, w)
            self.rect.y = random.randrange(-50, 0)
            self.speedy = random.randrange(3, 4)

    def newenemys(self):
        enemybadred = EnemyBadRed()
        all_sprites.add(enemybadred)
        enemysbadred.add(enemybadred)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, sx, sy):
        self.sx = sx
        self.sy = sy
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black)
        self.rect.x = random.randrange(0, w)
        self.rect.y = random.randrange(-50, 0)
        self.speedy = random.randrange(1, self.sy + 2)
        self.speedx = random.randrange(-2, 2)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > h + 15 or self.rect.left < -25 or self.rect.right > w + 20:
            self.rect.x = random.randrange(0, w)
            self.rect.y = random.randrange(-50, 0)
            self.speedy = random.randrange(3, 4)

    def newenemys(self, x, sx, sy):
        for i in range(x):
            enemy = Enemy(sx, sy)
            all_sprites.add(enemy)
            enemys.add(enemy)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ball_img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black)
        self.rect.center = (w / 2, h - 80)
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 2000:
            self.hidden = False
            self.rect.centerx = w / 2
            self.rect.bottom = h - 10
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -5
        if keys[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right >= w:
            self.rect.right = w
        elif self.rect.left < 0:
            self.rect.left = 0

    def hide(self):
        # временно скрыть игрока
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (w / 2, h + 200)
        screen.blit(fail_img, fail_rect)


class Heart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(live_img, (50, 50))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black)
        self.rect.x = random.randrange(0, w)
        self.rect.y = random.randrange(-50, 0)
        self.speedy = random.randrange(2, 5)
        self.speedx = random.randrange(-2, 2)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > h + 15 or self.rect.left < -25 or self.rect.right > w + 20:
            self.rect.x = random.randrange(0, w)
            self.rect.y = random.randrange(-50, 0)
            self.speedy = random.randrange(3, 4)

    def newheart(self):
        heart = Heart()
        all_sprites.add(heart)
        hearts.add(heart)


def text(bg_t, txt, size, x, y, color):
    font = pygame.font.Font(pygame.font.match_font('arial black'), size)
    font_c = font.render(txt, True, color)
    text_rect = font_c.get_rect()
    text_rect.midtop = (x, y)
    bg_t.blit(font_c, text_rect)


def start_screen():
    start_text = ['Добро пожаловать на гоночную трассу!',
                  'Судьба Молнии Маккуин ',
                  'зависит только от тебя!!',
                  'Своевременно обновляй резину,',
                  'остерегайся препятствий и злого ДПСника.',
                  'Набирай как можно больше очков',
                  'и переходи на следующий автодром!',
                  'Чтобы начать - нажми пробел']

    fon = pygame.image.load(os.path.join(img_dir, 'fon3.png')).convert()
    fon = pygame.transform.scale(fon, (760, 480))
    screen.blit(fon, bg_rect)
    font = pygame.font.Font(pygame.font.match_font('arial'), 30)
    text_rect = 50
    for line in start_text:
        string = font.render(line, 3, pygame.Color(black), pygame.Color(az))
        start_text_rect = string.get_rect()
        text_rect += 10
        start_text_rect.top = text_rect
        start_text_rect.center = w // 2, start_text_rect.y
        text_rect += start_text_rect.height
        screen.blit(string, start_text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        pygame.display.flip()
        clock.tick(fps)


def level_text(lvl):
    lvl_text = [f'Автодром {lvl}',
                'нажми пробел для продолжения']
    font = pygame.font.Font(pygame.font.match_font('arial black'), 25)
    text_rect = h // 3
    fon = pygame.image.load(os.path.join(img_dir, 'fon4.png')).convert()
    fon = pygame.transform.scale(fon, (760, 480))
    screen.blit(fon, bg_rect)

    for line in lvl_text:
        string_lvl = font.render(line, 1, pygame.Color(black), pygame.Color(az))
        start_text_rect = string_lvl.get_rect()
        text_rect += 10
        start_text_rect.top = text_rect
        start_text_rect.center = w // 2, start_text_rect.y
        text_rect += start_text_rect.height
        screen.blit(string_lvl, start_text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        pygame.display.flip()
        clock.tick(fps)


def fail(lvl):
    lvl_text = ['Так ты можешь лишиться прав..',
                '',
                f'Осталось покрышек: {lvl}',
                '',
                'Следи за дорогой!',
                'Чтобы продолжить - нажми пробел']
    font = pygame.font.Font(pygame.font.match_font('arial'), 25)
    text_rect = h // 3
    fon = pygame.image.load(os.path.join(img_dir, 'fon2.png')).convert()
    fon = pygame.transform.scale(fon, (760, 480))
    screen.blit(fon, bg_rect)

    for line in lvl_text:
        string_lvl = font.render(line, 1, pygame.Color(black), pygame.Color(az))
        start_text_rect = string_lvl.get_rect()
        text_rect += 10
        start_text_rect.top = text_rect
        start_text_rect.center = w // 2, start_text_rect.y
        text_rect += start_text_rect.height
        screen.blit(string_lvl, start_text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
        pygame.display.flip()
        clock.tick(fps)


def game_over(lvl):
    lvl_text = ['Кубок Поршня - твой! ',
                '',
                f'Пройдено автодромом: {lvl}',
                '',
                'Впереди только Формула 1!',
                '',
                'Для выхода нажми Esc']
    font = pygame.font.Font(pygame.font.match_font('arial'), 25)
    text_rect = h // 4
    fon = pygame.image.load(os.path.join(img_dir, 'fon3.png')).convert()
    fon = pygame.transform.scale(fon, (760, 480))
    screen.blit(fon, bg_rect)

    for line in lvl_text:
        string_lvl = font.render(line, 1, pygame.Color(black), pygame.Color(az))
        start_text_rect = string_lvl.get_rect()
        text_rect += 10
        start_text_rect.top = text_rect
        start_text_rect.center = w // 2, start_text_rect.y
        text_rect += start_text_rect.height
        screen.blit(string_lvl, start_text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()
        clock.tick(fps)


# координаты
w = 760
h = 480
fps = 60

# палитра
white = (255, 255, 255)
yellow = (255, 204, 0)
bg_c = (199, 10, 47)
sp_c = (126, 123, 245)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
az = (240, 255, 255)
df = (25, 25, 112)

pygame.init()

pygame.mixer.init()
screen = pygame.display.set_mode((w, h))

# подключение графики
img_dir = os.path.join(os.path.dirname(__file__), 'img')
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
ball_img = pygame.image.load(os.path.join(img_folder, 'car.png')).convert()
enemy_img = pygame.image.load(os.path.join(img_folder, 'con.png')).convert()
enemybad_img = pygame.image.load(os.path.join(img_folder, 'ment.png')).convert()
enemybadred_img = pygame.image.load(os.path.join(img_folder, 'znak.png')).convert()
fail_img = pygame.image.load(os.path.join(img_folder, 'stop.png')).convert()
fail_rect = fail_img.get_rect(center=(w // 2, h // 2))
live_img = pygame.image.load(os.path.join(img_folder, 'live.png')).convert()
live_img = pygame.transform.scale(live_img, (50, 50))
live_rect = live_img.get_rect(center=(50, 50))
live_img.set_colorkey(black)

# фон
bg = pygame.image.load(os.path.join(img_dir, 'race.png')).convert()
bg = pygame.transform.scale(bg, (760, 480))
bg_rect = bg.get_rect()

# подключение звука
snd_dir = os.path.join(os.path.dirname(__file__), 'snd')
good_meeting_snd = pygame.mixer.Sound(os.path.join(snd_dir, 'good.mp3'))
bad_meeting_snd = pygame.mixer.Sound(os.path.join(snd_dir, 'bad2.mp3'))
heart_meeting_snd = pygame.mixer.Sound(os.path.join(snd_dir, 'good2.mp3'))
badred_meeting_snd = pygame.mixer.Sound(os.path.join(snd_dir, 'bad.mp3'))
pygame.mixer.music.load(os.path.join(snd_dir, 'background.mp3'))
pygame.mixer.music.set_volume(0.4)

# описание игры
pygame.display.set_caption("Тачки")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
enemys = pygame.sprite.Group()
enemysbad = pygame.sprite.Group()
enemysbadred = pygame.sprite.Group()
hearts = pygame.sprite.Group()
ball = Ball()
all_sprites.add(ball)
for i in range(3):
    Enemy.newenemys(1, 1, 1, 1)
    EnemyBad.newenemys(1, 1, 1, 1)
score = 0
allscore = 3
life = 5
level = 1
fl_enemysbad = 0
fl_enemy = 0
fl_enemy_bad = 0
fl_enemy_bad_red = 0
pygame.mixer.music.play(loops=-1)

# игра
running = True
start_screen()
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    all_sprites.update()
    hits = pygame.sprite.spritecollide(ball, enemys, True)
    hitsBad = pygame.sprite.spritecollide(ball, enemysbad, True)
    hitsBadRed = pygame.sprite.spritecollide(ball, enemysbadred, True)
    hitsHeart = pygame.sprite.spritecollide(ball, hearts, True)

    for hit in hits:
        score += 1
        good_meeting_snd.play()

        if not fl_enemy:
            Enemy.newenemys(1, 2, 1 + level, 1 + level)
            fl_enemy = 1
        else:
            fl_enemy = 0

        if level > 2:
            if not fl_enemy_bad:
                EnemyBad.newenemys(1, 1, 1 + level, 1 + level)
                fl_enemy_bad = 1
            elif fl_enemy_bad < 3:
                fl_enemy_bad += 1
            else:
                fl_enemy_bad = 0

        if score >= 5:
            level += 1
            score = 0
            life = 5
            EnemyBadRed.newenemys(1)
            level_text(level)

    for hit in hitsBad:
        life -= 1
        bad_meeting_snd.play()

        if level < 3:
            if not fl_enemysbad:
                EnemyBad.newenemys(1, 1, 1 + level, 1 + level)
                fl_enemysbad = 1
            else:
                fl_enemysbad = 0
        else:
            EnemyBad.newenemys(1, 1, 1 + level, 1 + level)

        if life <= 1:
            Heart.newheart(1)

    for hit in hitsBadRed:
        badred_meeting_snd.play()
        life -= 2
        if life <= 1:
            Heart.newheart(1)

    for hit in hitsHeart:
        heart_meeting_snd.play()
        life += 1

    if life <= 0:
        allscore -= 1
        life = 5
        score = 0
        fail(allscore)

    if allscore <= 0:
        game_over(level)
        level = 1
        life = 5
        score = 0

    # Рендеринг
    screen.fill(bg_c)
    all_sprites.draw(screen)
    screen.fill(black)
    screen.blit(bg, bg_rect)
    screen.blit(live_img, live_rect)
    text(screen, str('Start'), 10, w // 8 * 7, 10, green)
    text(screen, str(score), 40, w // 8 * 7, 10, green)
    text(screen, str('Finish'), 10, w // 8 * 7.5, 10, red)
    text(screen, str(life), 40, w // 8 * 7.5, 10, red)
    text(screen, str(allscore), 30, 50, 25, white)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
