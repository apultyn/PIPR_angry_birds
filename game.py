import pygame
from side_programms import (
    get_list_enemies,
    change_angle
)
from sys import exit
from math import sin, cos, pi


def play(level):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Wściekłe Ptaki')
    clock = pygame.time.Clock()

    player_image = pygame.image.load('graphics/head.png').convert_alpha()
    player_surf = pygame.transform.scale(player_image, (50, 50))
    player_rect = player_surf.get_rect(center=(100, 600))

    enemy_image = pygame.image.load('graphics/enemy.png').convert_alpha()
    enemy_surf = pygame.transform.scale(enemy_image, (75, 50))

    grass_image = pygame.image.load('graphics/grass.png').convert_alpha()

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
                    list_of_enemies.remove(enemy)
                    player_rect = player_surf.get_rect(center=(100, 600))
                    fire = False
                    if list_of_enemies != []:
                        aim = True
                if (
                    player_rect.left < 0 or
                    player_rect.right > 1280 or
                    player_rect.top < 0 or
                    player_rect.bottom > 720
                ):
                    fire = False
                    player_rect = player_surf.get_rect(center=(100, 600))
                    tries -= 1
                    if tries > 0:
                        aim = True

            player_rect.centerx += Vx
            player_rect.centery -= Vy
            screen.blit(background, (0, 0))
            screen.blit(grass_image, (0, 0))
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
                        angle = change_angle('N', angle)
                    if event.key == pygame.K_s:
                        angle = change_angle('S', angle)
                    if event.key == pygame.K_a:
                        angle = change_angle('W', angle)
                    if event.key == pygame.K_d:
                        angle = change_angle('E', angle)
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
                        fire = True

            tries_show = font.render(f'Tries: {tries}', False, 'Black')
            force_show = font.render(f'Force: {force}', False, 'Black')

            screen.blit(background, (0, 0))
            screen.blit(grass_image, (0, 0))
            pygame.draw.line(
                screen,
                'Black',
                player_rect.center,
                (
                    player_rect.centerx + 200 * cos(angle * 2 * pi / 360),
                    player_rect.centery - 200 * sin(angle * 2 * pi / 360)
                ),
                width=10
            )
            screen.blit(tries_show, (1000, 100))
            screen.blit(force_show, (1000, 200))
            screen.blit(player_surf, player_rect)
            for enemy in list_of_enemies:
                screen.blit(enemy_surf, enemy.rect())

            pygame.display.update()
            clock.tick(60)
    if tries == 0:
        text_surf = font.render('You lost!', False, 'Black')
    if list_of_enemies == []:
        text_surf = font.render('You won!', False, 'Black')
    text_rect = text_surf.get_rect(center=(640, 360))
    screen.blit(background, (0, 0))
    screen.blit(grass_image, (0, 0))
    screen.blit(text_surf, text_rect)
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()


play(2)
