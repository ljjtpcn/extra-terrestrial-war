import sys
from random import randint

import pygame

from star import Star


def check_keys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, stars):
    """重绘屏幕"""
    screen.fill(settings.bg_color)
    stars.draw(screen)
    pygame.display.flip()


def get_number_stars_x(settings, star_width):
    space_x = settings.screen_width - star_width
    number_stars_x = int(space_x / (2 * star_width))
    return number_stars_x


def get_number_stars_y(settings, star_height):
    space_y = settings.screen_height - star_height
    number_stars_y = int(space_y / (2 * star_height))
    return number_stars_y


def create_star(screen, stars, star_number):
    star = Star(screen)
    star_width = star.rect.width
    star.x = randint(0, 1700) + star_width
    star.rect.x = star.x
    star.rect.y = randint(0, 700) + star.rect.height
    stars.add(star)


def create_stars(settings, screen, stars):
    star = Star(screen)
    number_stars_x = get_number_stars_x(settings, star.rect.width)
    number_stars_y = get_number_stars_y(settings, star.rect.height)
    # for row_number in range(number_stars_y):
    for star_number in range(number_stars_x):
        create_star(screen, stars, star_number)
