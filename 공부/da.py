import pygame
import sys
import random


pygame.init()
pygame.display.set_caption('비오는 게임')

Screen_x = 640 * 2
Screen_y = 480 * 2


screen = pygame.display.set_mode((Screen_x, Screen_y))

clock = pygame.time.Clock()

playing = True

image = pygame.image.load('back.png').convert_alpha()
image = pygame.transform.scale(image, (Screen_x, Screen_y))


class Rain:

    def __init__(self, x, y):
        self.x = x  # x
        self.y = y  # y
        self.speed = random.randint(10, 28)  # 속도
        self.bold = random.randint(1, 4)  # 굵기

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > Screen_y + 20

    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + 10), self.bold)


rains = []
for i in range(500):
    rains.append(Rain(random.randint(10, Screen_x - 10), 10))


while playing:

    """ 종료시 프로그램 종료시키는 코드 """

    for event in pygame.event.get():
        pass
        if event.type == pygame.QUIT:
            sys.exit()
    rains.append(Rain(random.randint(10, Screen_x - 10), 10))
    clock.tick(100)
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont('malgungothic', 30)
    a = font.render('''비 오는 게임 ㅎㅎ''', True, (25, 0, 0))
    screen.blit(a, (850, 150))  # 1. x, 2. y
    """빗방울 만들기"""
    for rain in rains:
        rain.move()
        rain.draw()
        if rain.off_screen():
            rains.remove(rain)
            del rain

    pygame.display.update()
