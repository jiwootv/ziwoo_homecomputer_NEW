# 오늘 만든 코드에서 사각형을 직사각형으로 만들고 회전을 시키기
# x 좌표가 화면을 넘어가면 0으로 만들기
# 부딧히면 반대 방향으로 팅기기
# 많이 부딪히면 사라지게 하기
# 색깔과 직사각형 모양 랜덤으로 만들기
# 볼륨 줄이기
# 스페이스 바를 놓았을 때 랜덤 으로 방향 설정
# 사각형 객체가 20개 이하가 되면 다시 생성
# 배경화면 추가해서 화면에 맞추어서 늘리기

# 각각을 지정한 코드에 주석을 달아서 코드를 완성하세요.
# 스페이스바를 연속으로 눌러 보세요.

import pygame
import random

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60  # Frame
GRAVITY = 0.3  # 중력값
SoundList = ["광.란.ogg", "JOJO chapter 7 Johnny Josuke.wav"]  # 1번 음악과 2번 음악 (1번 출처: https://youtu.be/Z2RnHPPwpWE 2번 출처: https://youtu.be/65rKikBS5eE)
STF = input('Drop sprite when space key is pressed (True or false) 스페이스 키를 눌렀을때 아바타 낙하')  # GRAVITI 사용(아래 참고)
SOUND_TF = input(' Play sound or No sound(True or false)')

BGM_TF = input('Play BGM or No BGM(True or false)')
if BGM_TF == 'True':
    Soundnum = int(input('Sound number(1: NHANKO GOD BGM  2: JOJO chapter 7 Johnny Josuke)'))
BACKGRAUND = int(input('BackGraund {1 or 2(1: Dark Knight 2: Forest)}'))
pygame.mixer.init()
if BGM_TF == 'True':
    sound = pygame.mixer.Sound(SoundList[Soundnum - 1])
    sound.play(-1)


class Figure(pygame.sprite.Sprite):  # 스프라이트
    def __init__(self, root):
        self.game = root
        self.image = pygame.Surface((random.randint(10, 30), random.randint(10, 30)))
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.image_t = self.image
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = pygame.Vector2(random.randint(0, SCREEN_X), random.randint(0, SCREEN_Y))
        self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)
        self.speed = 2
        self.rotate = 0
        self.rotate_speed = random.randint(1, 3)
        self.col_lim = random.randint(0, 5) * -1

    def update(self):
        self.rotate += self.rotate_speed
        self.image = pygame.transform.rotozoom(self.image_t, self.rotate, 1)
        self.image.set_colorkey((0, 0, 0))
        if self.game.pressed_key[pygame.K_SPACE] and STF == 'True':  # 스페이스 누르면 11m에서 떨어지는 모형탑훈련
            self.dir.y += GRAVITY

            self.pos += self.dir * self.speed
            if self.pos.y > SCREEN_Y:
                self.pos.y = SCREEN_Y - 10

            self.rect.center = self.pos
        else:
            if self.pos.x > SCREEN_X:
                self.pos.x = 0
            if self.pos.x < 0:
                self.pos.x = SCREEN_X
            if self.pos.y > SCREEN_Y:
                self.pos.y = 0
            if self.pos.y < 0:
                self.pos.y = SCREEN_Y
            self.dir = self.dir.normalize()
            self.pos += self.dir * self.speed
            self.rect.center = self.pos

        if self.col_lim > 3:
            self.kill()
            del self

    #def col123(self):
        #self.dir = self.dir * -1
        #self.col_lim += 1  (아쉽게 삭제)

    def reset(self):
        self.dir = pygame.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('화면 보호기 / 멍때리기')
        self.img = ['DARK Knight.svg', 'back.png']  # 배경
        # self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        if not STF == 'True':
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # 전체화면
        else:
            self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 1280x960
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.bomb = pygame.mixer.Sound('Boing.wav')
        self.bomb.set_volume(0.1)
        self.back = pygame.image.load(self.img[BACKGRAUND - 1])
        self.back = pygame.transform.scale(self.back, (SCREEN_X, SCREEN_Y))
        self.F = Figure(self)

    def run(self):
        while self.playing:  # 실행
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):  # 하.하.하
        self.pressed_key = pygame.key.get_pressed()
        # 종료 코드
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

        for figure in self.all_sprites:
            re = pygame.sprite.spritecollide(figure, self.all_sprites, False)
            for a in re:
                if not figure == a and SOUND_TF == 'True':
                    pygame.mixer.Sound.play(self.bomb)
                    Figure.col123(self.F)  # 잊혀진 그것...

    def update(self):
        if len(self.all_sprites) < 20:
            self.all_sprites.add(Figure(self))
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.back, (0, 0))
        self.all_sprites.draw(self.screen)


game = Game()
game.run()
pygame.quit()
