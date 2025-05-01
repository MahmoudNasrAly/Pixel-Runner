import pygame

from src.services.visualization_service import VisualizationService
from src.config import Config
from src.components.game_status import GameStatus
from src.game_phases import main_menu_phase, gameplay_phase, exit_game_phase
from src.global_state import GlobalState


pygame.init()


FramePerSecond = pygame.time.Clock()


def update_display_screen():
    pygame.display.update()
    FramePerSecond.tick(Config.FPS)


def main():

    while True:
        if GlobalState.GAME_STATE == GameStatus.MAIN_MENU:
            main_menu_phase()
        if GlobalState.GAME_STATE == GameStatus.GAMEPLAY:
            gameplay_phase()
        if GlobalState.GAME_STATE == GameStatus.GAME_END:
            exit_game_phase()
        
        update_display_screen()

if __name__ == "__main__":
    main()
