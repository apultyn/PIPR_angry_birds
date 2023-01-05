import pygame
import side_programms
from sys import exit
from math import sin, cos, pi



pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Wściekłe Ptaki')
clock = pygame.time.Clock()

player_surf = pygame.image.load('graphics/head.png').convert_alpha()
player_rect = player_surf.get_rect(center=(200, 360))

enemy_surf = pygame.image.load('graphics/enemy.png').convert_alpha()
enemy_rect = player_surf.get_rect(center=(1000, 360))

background = pygame.image.load('graphics/background.png')
font = pygame.font.Font(None, 50)
tries = 5
force = 50
angle = 0
aim = True

while tries > 0:
    while aim == True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    angle = side_programms.change_angle('S', angle)
                if event.key == pygame.K_s:
                    angle = side_programms.change_angle('N', angle)
                if event.key == pygame.K_a:
                    angle = side_programms.change_angle('W', angle)
                if event.key == pygame.K_d:
                    angle = side_programms.change_angle('E', angle)
                if event.key == pygame.K_SPACE:



        tries_show = font.render(f'Tries: {tries}', False, 'Black')
        force_show = font.render(f'Force: {force}', False, 'Black')
        # angle_show = font.render(f'Angle: {angle}', False, 'Black')


        screen.blit(background, (0, 0))
        screen.blit(tries_show, (1000, 100))
        screen.blit(force_show, (1000, 200))
        # screen.blit(angle_show, (1000, 300))
        screen.blit(player_surf, player_rect)
        screen.blit(enemy_surf, enemy_rect)
        pygame.draw.line(screen,
                        'Red',
                        player_rect.center,
                        (
                            player_rect.centerx + 200 * cos(angle * 2 * pi / 360),
                            player_rect.centery + 200 * sin(angle * 2 * pi / 360)
                        ),
                        10
                        )

        pygame.display.update()
        clock.tick(10)
