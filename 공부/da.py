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


class Rain:

    def __init__(self, x, y):
        self.x = x  # x
        self.y = y  # y
        self.speed = random.randint(10, 108)  # 속도
        self.bold = random.randint(1, 4)    #굵기

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > Screen_y + 20

    def draw(self):
        pygame.draw.line(screen, (10, 1, 8), (self.x, self.y), (self.x, self.y + 10), self.bold)


rains = []
for i in range(3500):
    rains.append(Rain(random.randint(10, Screen_x - 10), 10))

while playing:

    """종료시 프로그램 종료시키는 코드"""
    for event in pygame.event.get():
        pass
        if event.type == pygame.QUIT:
            sys.exit()
    rains.append(Rain(random.randint(10, Screen_x - 10), 10))
    clock.tick(60)
    screen.fill((255, 255, 255))
    """빗방울 만들기"""
    for rain in rains:
        rain.move()
        rain.draw()
        if rain.off_screen():
            rains.remove(rain)
            del rain

    pygame.display.update()