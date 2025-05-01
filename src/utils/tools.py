import pygame
import math


def sine(speed: float, time: int, how_far: float, overall_y: int):
    t = pygame.time.get_ticks() / 2 % time
    y = math.sin(t / speed) * how_far + overall_y
    return int(y)


def is_close_app_event(event):
    return (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
