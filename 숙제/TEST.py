import pygame
import pygame.font
import random

pygame.init()
Screen_x = 640
Screen_y = 640
pygame.display.set_mode((Screen_x, Screen_y))
# screen = pygame.display.set_mode((Screen_x, Screen_y))
pygame.display.set_caption('뽑기')


class Rotto:
    def __init__(self):
        self.randomnum = [0, 0, 0, 0, 0, 0]
        self.screen = pygame.display.set_mode((Screen_x, Screen_y))
        self.plyernum = []
        self.score = 0
        self.string = ''

    def random(self):  # 1
        self.randomnum = [random.randint(1, 63), random.randint(1, 63), random.randint(1, 63), random.randint(1, 63),
                          random.randint(1, 63), random.randint(1, 63)]
        for num in range(0, 6):
            self.plyernum.append(int(input('숫자(1부터 63사이의 숫자)')))

    def godog_zoayo(self):  # 2
        for i in range(0, 6):
            if self.plyernum[i] == self.randomnum[i]:
                self.score += 1
        self.string = '점수는 ', self.score, '점 입니다.'
        self.draw_text(self, self.string, [0,0,100], 0)

    def draw_text(self, text, color, x, y):
        font = pygame.font.SysFont('malgungothic', 20)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.screen.blit(text_surface, text_rect)

    def run(self):
        self.random()
        self.godog_zoayo()


r = Rotto()

Rotto.run(r)




