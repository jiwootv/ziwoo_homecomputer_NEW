# 파이게임 기본 코드
import pygame.font
import pygame
import random

vec = pygame.Vector2

pygame.init()
pygame.display.set_caption('게임 제목')
Screen_x = 640  # 화면 넓이
Screen_y = 480  # 화면 높이

def draw_text(surface, text, size, color, x, y):
    font = pygame.font.SysFont('malgungothic', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    text_rect.y = y
    surface.blit(text_surface, text_rect)

class Ui(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.groups = self.game.ui
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((Screen_x, Screen_y))
        self.rect = self.image.get_rect()

        self.image.set_colorkey('Black')

        self.ui_health = self.game.sa.health

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('malgungodic', size)
        text_suface = font.render(text, True, color)
        text_rect = text_suface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.image.blit(text_suface, text_rect)

    def update(self):
        self.image.fill('Black')
        pygame.draw.rect(self.image, 'Gray', (0, 0, Screen_x + 3, Screen_y + 18), 10, 10)
        self.ui_health = self.game.sa.health
        pygame.draw.line(self.image, 'Sky blue', (100, Screen_y - 100), (100 + self.ui_health, Screen_y - 100), 15)
        self.draw_text(f'Hp: {self.ui_health}', 40, pygame.Color('Blue'), 0, 0)


# 파이게임 기본 코드(클래스)


class Sa(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.image = pygame.image.load('player ().png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        # self.image = pygame.Surface((200, 50))
        # self.image.fill('Red')
        self.image_t = self.image
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect.centerx = Screen_x / 2
        self.rect.centery = Screen_y / 2
        self.rect.centerx += 1
        self.angle = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.math.Vector2(0, 0)
        self.x123 = 1
        self.health = 300
        self.move = 10

    def update(self):
        self.image = pygame.transform.rotozoom(self.image_t, self.angle, 1)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        if self.pos.x > Screen_x:
            self.pos.x = 0
        self.x123 += 0
        self.pos.y = Screen_y * 8 / 10
        self.rect.centerx = Screen_x / 2
        if self.game.pressed_key[pygame.K_RIGHT]:
            self.pos.x += self.move
        if self.game.pressed_key[pygame.K_LEFT]:
            self.pos.x -= self.move
        self.rect.centery = Screen_y * 8 / 10
        self.rect.center = self.pos


class Rain(pygame.sprite.Sprite):
    def __init__(self, x, y, root):
        self.speed = random.randint(5, 28)
        self.bold = random.randint(1, 4)
        self.game = root
        self.len = random.randint(5, 15)
        self.random_color = pygame.Color('skyblue')
        self.random_color = random.randint(0, 7)
        self.groups = self.game.rains, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((self.bold, self.len))
        self.color123 = ['Red', 'orange', 'yellow', 'green', 'skyblue', 'blue', 'purple', 'gray']
        self.image.fill(self.color123[self.random_color])
        self.item_sound = pygame.mixer.Sound('Bite.wav')
        self.speed_sound_up = pygame.mixer.Sound('Connect.wav')
        self.speed_sound_down = pygame.mixer.Sound('Connect2.wav')

        self.pos = vec(x, y)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.random_number = 0
        self.bool = [False, False]
        self.bool_v = 0
        self.randomnum = 0

    def randomcode(self):
        self.random_number = random.randint(0, 8)
        if self.random_number == 0:
            self.game.sa.health -= 10
            self.game.hit_sound.play()
            self.kill()
            del self
            return
        if self.random_number == 1:
            self.game.sa.move += 0.2
            self.speed_sound_up.play()
            self.kill()
            print(game.sa.move)
            del self
            return
        if self.random_number == 2:
            self.game.sa.move -= 0.2
            self.speed_sound_down.play()
            self.kill()
            print(game.sa.move)
            del self
            return
        if self.random_number == 3:
            self.game.sa.health += 5
            self.speed_sound_down.play()
            self.kill()
            print(game.sa.move)
            del self
            return
        pass

    def update(self):

        if pygame.sprite.collide_mask(self, self.game.sa):
            if self.random_color == 0:  # 순서대로 빨 주 노 초 파 람 보 검(회색)
                self.game.sa.health -= 10
                self.game.hit_sound.play()
                self.kill()
                del self
                return
            if self.random_color == 1:
                self.randomnum = random.randint(1, 2)
                if self.randomnum == 1 and self.game.sa.move > 2:
                    self.game.sa.move -= 2
                    self.speed_sound_down.play()
                    self.kill()
                    print(game.sa.move)
                    del self
                    return
                return
            if self.random_color == 2:
                self.randomnum = random.randint(1, 2)
                if self.randomnum == 1:
                    self.game.sa.move += 2
                    self.speed_sound_up.play()
                    self.kill()
                    print(game.sa.move)
                    del self
                    return
            if self.random_color == 3:
                self.game.sa.health += 5
                self.item_sound.play()
                self.kill()
                print(game.sa.move)
                del self
                return




        self.pos.y += self.speed
        self.rect.topleft = self.pos
        if self.off_screen():
            self.kill()
            del self
            return

    def off_screen(self):
        return self.rect.y > Screen_y + 20


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('하늘에서 비가 쏟아진다면')
        self.pressed_key = pygame.key.get_pressed()
        self.screen = pygame.display.set_mode((Screen_x, Screen_y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.sa = Sa(self)
        self.rains = pygame.sprite.Group()
        self.ui = pygame.sprite.GroupSingle()
        self.ui.add(Ui(self))
        self.bg = pygame.image.load(('모양 3 (1).svg'))
        self.bg = pygame.transform.scale(self.bg, (Screen_x, Screen_y))
        pygame.mixer.init()
        pygame.mixer.music.load('용구탄생의 비밀.mp3')
        pygame.mixer.music.set_volume(1.3)

        self.camera = vec(0, 0)
        self.bgcamera = vec(0, 0)
        self.hit_sound = pygame.mixer.Sound('Crunch.wav')
        self.Lose = pygame.mixer.Sound('MP_롤 패배 음성.mp3')



        self.end_time = 0
        self.end_on = False
        self.score = 0

    def run(self):
        pygame.mixer.music.play(-1)

        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()

            pygame.display.update()

    def event(self):
        self.pressed_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        self.rains.add(Rain(random.randint(0, Screen_x), 100, self))

    def update(self):
        if Screen_x / 8 * 2 > self.sa.pos.x:
            self.camera.x = -self.sa.move
        elif Screen_x * 6 / 8 < self.sa.pos.x:
            self.camera.x = self.sa.move
        else:
            self.camera.x = 0
        for sprite in self.all_sprites:
            sprite.pos.x -= self.camera.x
        self.bgcamera += self.camera
        self.all_sprites.update()
        self.ui.update()
        if self.sa.health < 0:
            if self.end_on == False:
                self.end_time = pygame.time.get_ticks()
                self.end_on = True
            draw_text(self.bg, "GAME OVER...", 50, pygame.Color('Blue'), 120, 240)

            print(self.score)

            if pygame.time.get_ticks() - self.end_time > 4000:
                self.playing = False
    def draw(self):
        self.screen.fill((255, 255, 0))
        for n in range(5000):
            self.screen.blit(self.bg, (Screen_x * (n - 2) - self.bgcamera.x, 0))
        self.all_sprites.draw(self.screen)
        self.ui.draw(self.screen)


game = Game()
game.run()
pygame.quit()