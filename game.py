import pygame
import side_programms
from sys import exit
from math import sin, cos, pi


class Enemy:
    def __init__(self, pos):
        self._pos = pos
        self._rect = None

    def __str__(self):
        return str(self._pos)

    def pos(self):
        return self._pos

    def rect(self):
        return self._rect


def get_list_enemies(level):
    if int(level) == 1:
        one = Enemy((1000, 360))
        return [one]
    if int(level) == 2:
        one = Enemy((1000, 360))
        two = Enemy((1000, 660))
        return [one, two]


def play(level):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Wściekłe Ptaki')
    clock = pygame.time.Clock()

    player_surf = pygame.image.load('graphics/head.png').convert_alpha()
    player_rect = player_surf.get_rect(center=(100, 360))

    enemy_surf = pygame.image.load('graphics/enemy.png').convert_alpha()

    list_of_enemies = get_list_enemies(level)
    for enemy in list_of_enemies:
        enemy._rect = enemy_surf.get_rect(center=enemy.pos())

    background = pygame.image.load('graphics/background.png')
    font = pygame.font.Font(None, 50)
    tries = 5
    force = 50
    angle = 0
    aim = True
    fire = False
    Vx = 0
    Vy = 0
    while tries > 0 and list_of_enemies != []:
        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            for enemy in list_of_enemies:
                if player_rect.colliderect(enemy.rect()):
                    print(f'Collided with {enemy}')
                    list_of_enemies.remove(enemy)
                    player_rect = player_surf.get_rect(center=(100, 360))
                    fire = False
                    if list_of_enemies != []:
                        aim = True
                if player_rect.left < 0 or player_rect.right > 1280 or player_rect.top < 0 or player_rect.bottom > 720:
                    fire = False
                    player_rect = player_surf.get_rect(center=(100, 360))
                    tries -= 1
                    if tries > 0:
                        aim = True

            player_rect.centerx += Vx
            player_rect.centery -= Vy
            screen.blit(background, (0, 0))
            screen.blit(player_surf, player_rect)
            for enemy in list_of_enemies:
                screen.blit(enemy_surf, enemy.rect())
            pygame.display.update()
            Vy -= 2
            clock.tick(60)
        while aim:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        angle = side_programms.change_angle('N', angle)
                    if event.key == pygame.K_s:
                        angle = side_programms.change_angle('S', angle)
                    if event.key == pygame.K_a:
                        angle = side_programms.change_angle('W', angle)
                    if event.key == pygame.K_d:
                        angle = side_programms.change_angle('E', angle)
                    if event.key == pygame.K_UP:
                        if force < 100:
                            force += 5
                    if event.key == pygame.K_DOWN:
                        if force > 0:
                            force -= 5
                    if event.key == pygame.K_SPACE:
                        aim = False
                        Vx = force * cos(angle * 2 * pi / 360) / 2
                        Vy = force * sin(angle * 2 * pi / 360) / 2
                        print(angle, Vx, Vy)
                        fire = True

            tries_show = font.render(f'Tries: {tries}', False, 'Black')
            force_show = font.render(f'Force: {force}', False, 'Black')
            # angle_show = font.render(f'Angle: {angle}', False, 'Black')

            screen.blit(background, (0, 0))
            screen.blit(tries_show, (1000, 100))
            screen.blit(force_show, (1000, 200))
            # screen.blit(angle_show, (1000, 300))
            screen.blit(player_surf, player_rect)
            for enemy in list_of_enemies:
                screen.blit(enemy_surf, enemy.rect())
            pygame.draw.line(
                screen,
                'Red',
                player_rect.center,
                (
                    player_rect.centerx + 200 * cos(angle * 2 * pi / 360),
                    player_rect.centery - 200 * sin(angle * 2 * pi / 360)
                ),
                width=10
            )

            pygame.display.update()
            clock.tick(60)
    print('End')


play(2)
