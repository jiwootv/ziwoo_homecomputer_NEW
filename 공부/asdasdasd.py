y = 150
x = 505
import pygame, sys

pygame.init()


sound = pygame.mixer.Sound('넌-모찌나간다-_방패병_.wav')
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1300, 600))
chracter_img = pygame.image.load('sans2 (1).svg')
i_x, i_y = chracter_img.get_size()
font = pygame.font.SysFont('malgungothic', 50)

key = 0
key_y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # x += random.randint(1,10)
        if event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_a or pygame.K_RIGHT):
                key = -1

            if event.key == (pygame.K_d or pygame.K_LEFT):
                key = 1
            if event.key == (pygame.K_s or pygame.K_DOWN):
                key_y = 1
            if event.key == (pygame.K_w or pygame.K_UP):
                key_y = -1

        if event.type == pygame.KEYUP:
            key = 0
            key_y = 0
        if x > 1300:
            x = 650
    x += key
    y += key_y
    screen.fill((255, 255, 255))
    a = font.render(f'x 좌표: {x} y 좌표:{y}', True, (255, 0, 0))
    screen.blit(chracter_img, (x, y))
    screen.blit(a, (650, 150))
    if x > 1300 - i_x:
        x = 0
        sound.play()
    if 0 > x:
        x = 1300 - i_x
        sound.play()
    if y > 600 - i_y:
        y = 0
        sound.play()
    if 0 > y:
        y = 600 - i_y
        sound.play()
    clock.tick(60)
    pygame.display.update()
