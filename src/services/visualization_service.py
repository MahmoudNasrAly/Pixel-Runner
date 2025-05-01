import pygame

from paths import ASSESTS_DIR, MENU_DIR
from src.config import Config
from src.utils.tools import sine


class VisualizationService:

    @staticmethod
    def get_background_image():
        return pygame.image.load(ASSESTS_DIR / 'background.png').convert_alpha()

    @staticmethod
    def get_ground_image():
        return pygame.image.load(ASSESTS_DIR / 'ground.png').convert_alpha()

    @staticmethod
    def get_owl_image():
        return pygame.image.load(ASSESTS_DIR / 'owl.png').convert_alpha()

    @staticmethod
    def get_spider_image():
        return pygame.image.load(ASSESTS_DIR / 'spider.png').convert_alpha()

    @staticmethod
    def get_palyer_image():
        return pygame.image.load(ASSESTS_DIR / 'nagato.png').convert_alpha()

    @staticmethod
    def get_title_image():
        return pygame.image.load(MENU_DIR / 'title.png').convert_alpha()

    @staticmethod
    def get_press_any_key_image():
        return pygame.image.load(MENU_DIR / 'press_any_button.png').convert_alpha()

    @staticmethod
    def get_credit_font():
        return pygame.font.Font(ASSESTS_DIR / 'Pixeltype.ttf', 40)

    @staticmethod
    def get_score_font():
        return pygame.font.Font(ASSESTS_DIR / 'Pixeltype.ttf', 30)

    @staticmethod
    def get_main_font():
        return pygame.font.Font(ASSESTS_DIR / 'Pixeltype.ttf', 40)

    @staticmethod
    def load_main_display():
        pygame.display.set_caption("Pixel Runner")
        icon = VisualizationService.get_palyer_image()
        pygame.display.set_icon(icon)

    @staticmethod
    def draw_background(screen):
        background = VisualizationService.get_background_image()
        screen.blit(background, (0, 0))

    @staticmethod
    def draw_ground(screen):
        ground = VisualizationService.get_ground_image()
        screen.blit(ground, (0, 400))

    @staticmethod
    def draw_best_score(screen, max_score):
        score_font = VisualizationService.get_credit_font()
        score_text = score_font.render(f"Best: {max_score}", False, "Black")
        score_rect = score_text.get_rect(center=(Config.WIDTH // 2, 250))
        screen.blit(score_text, score_rect)

    @staticmethod
    def draw_author_credit(screen):
        credit_font = VisualizationService.get_credit_font()
        author_credit = credit_font.render("Made by Mahmoud Nasr", False, "White")
        author_credit_rect = author_credit.get_rect(
            center=(Config.WIDTH // 2, 500))
        screen.blit(author_credit, author_credit_rect)

    @staticmethod
    def draw_title(screen):
        y = sine(200.0, 1280, 10.0, 50)
        title = VisualizationService.get_title_image()
        screen.blit(title, (204, y))

    @staticmethod
    def draw_press_any_key(screen):
        y = sine(100.0, 1280, 10.0, 190)
        press_any_key = VisualizationService.get_press_any_key_image()
        screen.blit(press_any_key, (y, 350))

    @staticmethod
    def draw_main_menu(screen, max_score):
        VisualizationService.draw_background(screen)
        VisualizationService.draw_ground(screen)
        VisualizationService.draw_author_credit(screen)
        VisualizationService.draw_best_score(screen, max_score)
        VisualizationService.draw_title(screen)
        VisualizationService.draw_press_any_key(screen)

    @staticmethod
    def draw_gameplay_background(screen):
        VisualizationService.draw_background(screen)
        VisualizationService.draw_ground(screen)
