import sys
import pygame
import time

from src.global_state import GlobalState
from src.components.game_status import GameStatus
from src.services.visualization_service import VisualizationService
from src.utils.tools import is_close_app_event
from src.components.player import Player
from src.components.enemy import Enemy
from src.components.scoreboard import ScoreBoard
from src.components.enemy_type import EnemyType



GlobalState.load_main_screen()
VisualizationService.load_main_display()

scoreboard = ScoreBoard()

# Gropus
P1 = Player()
OWL = Enemy(EnemyType.OWL)
SPIDER = Enemy(EnemyType.SPIDER)
enemies = pygame.sprite.Group()
enemies.add(OWL)
enemies.add(SPIDER)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(OWL)
all_sprites.add(SPIDER)


def main_menu_phase():

    scoreboard.reset()
    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return
        if event.type == pygame.KEYDOWN:
            GlobalState.GAME_STATE = GameStatus.GAMEPLAY

    VisualizationService.draw_main_menu(GlobalState.SCREEN, scoreboard.get_max_score())


def gameplay_phase():

    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.MAIN_MENU
            game_over()
            return
    
    P1.update()
    OWL.move(scoreboard)
    SPIDER.move(scoreboard)

    VisualizationService.draw_gameplay_background(GlobalState.SCREEN)

    P1.draw(GlobalState.SCREEN)
    OWL.draw(GlobalState.SCREEN)
    SPIDER.draw(GlobalState.SCREEN)
    scoreboard.draw(GlobalState.SCREEN)

    if pygame.sprite.spritecollide(P1, enemies, False, pygame.sprite.collide_mask):
        scoreboard.update_max_score()
        time.sleep(0.5)
        game_over()

def exit_game_phase():
    pygame.quit()
    sys.exit()


def game_over():
    GlobalState.GAME_STATE = GameStatus.MAIN_MENU
    P1.reset()
    OWL.reset()
    SPIDER.reset()
    time.sleep(0.5)
