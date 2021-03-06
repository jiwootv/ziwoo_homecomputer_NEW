# 파이게임 기본(클래스)
# By jiwootv
import pygame, random, os

# 전역상수
SCREEN_X = 640  # 화면 넓이
SCREEN_Y = 480  # 화면 높이
FPS = 60
vec = pygame.math.Vector2

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (320, 30)


def draw_text(surface, text, size, color, x, y):
    font = pygame.font.SysFont('malgungothic', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

class MogiGuzer(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('모기꺼져_LOCK.png')
        self.image = pygame.transform.scale(self.image , (400, 200))
        self.rect = self.image.get_rect(center=(600, 370))
        self.game = root
        self.groups = self.game.all_sprite
        pygame.sprite.Sprite.__init__(self, self.groups)

class Mogi(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('모양 1 (2).png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprite, self.game.mogi
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect.center = (100, 30)
        self.pos = vec(random.randint(0, SCREEN_X), 50)
        self.dir = vec(0, 0)
        self.time = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)
        self.v_bool = True
        self.mogi_kiil_sound = pygame.mixer.Sound('공부_Pygam_따귀+세게_t.wav')
        self.sec = 100

    def update(self):
        self.dir = vec(random.random() * random.randint(-20, 20), random.random() * random.randint(-20, 20))
        if pygame.time.get_ticks() - self.time < 2000:
            self.time = pygame.time.get_ticks()
            self.pos += self.dir
            self.rect.center = self.pos
        if self.pos.x < 0 or self.pos.x > SCREEN_X:
            self.kill()
            del self
            return
        self.event()

    def event(self):
        if pygame.sprite.collide_mask(self, self.game.stick) and pygame.mouse.get_pressed(3)[0] and self.v_bool:
            self.game.mogi_kill += 1
            pygame.mixer.init()
            self.mogi_kiil_sound.play()
            self.mogi_kiil_sound.set_volume(0.6)

            self.kill()
            del self
            return
        if pygame.mouse.get_pressed(3)[0] == True:
            self.v_bool = False


        else:
            self.v_bool = True

    def timer(self):
        self.sec = 100
        # self.


class Mogistick(pygame.sprite.Sprite):
    def __init__(self, root):  #
        self.image = pygame.image.load('mogi_stic.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprite, self.game.mogichea
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect.center = (100, 30)
        self.pos = vec(random.randint(0, SCREEN_X), 50)
        self.dir = vec(0, 0)
        self.time = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.rect.bottomright = self.pos - vec(-22, -23)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprite = pygame.sprite.Group()
        self.mogi = pygame.sprite.Group()
        self.mogichea = pygame.sprite.Group()
        self.stick = Mogistick(self)
        self.all_sprite.add(self.stick)
        self.mogichea.add(self.stick)
        self.mogiguzer = MogiGuzer(self)
        self.all_sprite.add(self.mogiguzer)
        self.mogi_num = 30
        self.mogi_kill = 0
        self.stop = True
        self.fullscreen = False
        self.stage = 10
        self.mogi_if = 0
        self.time = pygame.time.get_ticks()
        pygame.mixer.music.load('용구탄생의 비밀.wav')
        self.mogi_plus = 20
        self.time_minus = 100
        self.bgm1 = 0
        self.next_bool = [True, True, True, True, True]
        self.mogiguzer_use_number = 0
        self.mogiguzer_sound = pygame.mixer.Sound('효과음-_-부왘.wav')
        print(self.mogi_if + self.mogi_plus)

    def run(self):
        self.opning()
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1.0)
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

            pygame.display.update()

    def event(self):
        # 종료 코드
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_F11 and self.fullscreen:
                    self.fullscreen = False
                    pygame.display.toggle_fullscreen()
                    self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 0)

                    break
                if event.key == pygame.K_F11 and not self.fullscreen:
                    self.fullscreen = True
                    self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), pygame.FULLSCREEN)
                if event.key == pygame.K_m and 10 < self.stage:
                    self.mogiguzer.image = pygame.image.load('모기꺼져.png')
                    self.mogi_num -= 40
                    self.mogi_kill += 40
                    self.mogiguzer_sound.play()
                    self.mogiguzer_use_number += 1
                    print(len(self.mogi))
                    for mogi in self.all_sprite:
                        if mogi in self.mogi:
                            mogi.kill()
                            del mogi
                    print(len(self.mogi))



    def update(self):
        self.all_sprite.update()
        if len(self.mogi) < self.mogi_num:
            self.mogi_sprite = Mogi(self)
            self.all_sprite.add(self.mogi_sprite)
            self.mogi.add(self.mogi_sprite)
        if self.mogi_kill > self.mogi_if + self.mogi_plus:
            self.mogi_plus += self.stage * 10
            self.stage += 1
            self.time_minus += int(self.time / 1000 + 10)
            del self
            return
        if self.stage == 5 and self.next_bool[0]:

            self.screen.fill((255, 255, 255))
            draw_text(self.screen, '"최근, 모기가 갑자기 자취를 감췄습니다."', 20, pygame.Color('Blue'), 250, 30)
            draw_text(self.screen, '"모기 연구진들은 모기가 알수 없는 이유로 자취를 감취었다고 생각합니다."', 10, pygame.Color('Blue'), 300, 60)
            draw_text(self.screen, '이게 뭔 소식인가.. 나 그냥 친구가 뉴스 보라고 해서 본 건데.. 근데 또 들어왔잖아!!!', 10, pygame.Color('Blue'), 300, 90)
            draw_text(self.screen, '스페이스바를 눌러 시작', 50, pygame.Color('Blue'), 300, 180)
            pygame.display.flip()
            self.time_stop()
            self.next_bool[0] = False
        if self.stage == 10 and self.next_bool[1]:
            self.screen.fill((255, 255, 255))
            print(self.next_bool)
            draw_text(self.screen, '"... 최근 모기가 다시 시민을 공격하고 있습니다."', 20, pygame.Color('Blue'), 250, 30)
            draw_text(self.screen, '"아무래도 인간을 속이기 위한 작전이였던 것같습니다.. 그래서 살충제 모기꺼져를 드리겠습니다."', 10, pygame.Color('Blue'), 300, 60)
            draw_text(self.screen, '이게 뭔 소식인가.. 나 그냥 친구가 뉴스 보라고 해서 본 건데.. 아... 언제 끝나..', 10, pygame.Color('Blue'), 300, 90)
            draw_text(self.screen, '스페이스바를 눌러 시작', 50, pygame.Color('Blue'), 300, 180)
            pygame.display.flip()
            self.next_bool[1] = False
            self.time_stop()

        if self.mogi_num <= 0:
            self.mogi_num = self.mogi_if + self.mogi_plus
            self.mogi_kill = 0
        if self.mogiguzer_use_number > 5:

            self.screen.fill((0, 0, 0))
            draw_text(self.screen, '당신은 모기꺼져에 들어있던 방귀 때문에 죽었습니다..', 20, pygame.Color('Blue'), SCREEN_X/2, SCREEN_Y / 2)
            draw_text(self.screen, '엔딩: 모기꺼져좀 적당히 쓰세요(엔딩 1, 히든엔딩)', 20, pygame.Color('Blue'), SCREEN_X/2, SCREEN_Y / 3)
            pygame.display.flip()
            self.time_stop()
            pygame.quit()








    def draw(self):
        self.screen.fill(pygame.Color('White'))
        self.all_sprite.draw(self.screen)
        draw_text(self.screen, f'모기 잡은 수: {self.mogi_kill}', 30, pygame.Color('Blue'), 100, 10)
        self.time = pygame.time.get_ticks()
        draw_text(self.screen, f'남은 시간: {self.time_minus - int(self.time / 1000)}', 20, pygame.Color('Black'), 120, 90)
        draw_text(self.screen, f'잡아야 하는 모기:: {(self.mogi_if + self.mogi_plus) - self.mogi_kill + 1}', 20,
                  pygame.Color('Black'), 450, 90)
        draw_text(self.screen, f'스테이지: {self.stage}', 30, pygame.Color('Blue'), 100, 400)

    def time_stop(self):
        self.stop = True
        while self.stop:
            self.clock.tick(60)
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[pygame.K_SPACE]:
                self.stop = False


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop = False
                    self.playing = False


    def opning(self):
        draw_text(self.screen, '어느 날... 별 차이 없는 평범한 날.. 흘러나오는 뉴스..', 20, pygame.Color('Blue'), 150, 30)
        draw_text(self.screen, '"최근, 모기의 개체수가 급격하게 늘어났습니다."', 20, pygame.Color('Blue'), 240, 60)
        draw_text(self.screen, '이게 뭔 소식인가.. 나 그냥 친구가 뉴스 보라고 해서 본 건데..', 20, pygame.Color('Blue'), 300, 90)
        draw_text(self.screen, '스페이스바를 눌러 시작', 50, pygame.Color('Blue'), 300, 180)
        pygame.display.flip()
        self.time_stop()


game = Game()
game.run()
pygame.quit()
