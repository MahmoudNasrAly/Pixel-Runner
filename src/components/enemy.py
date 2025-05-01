import pygame
import random

from src.components.scoreboard import ScoreBoard
from src.components.enemy_type import EnemyType
from src.services.visualization_service import VisualizationService
from src.config import Config


class Enemy(pygame.sprite.Sprite):

    def __init__(self, enemy_type: EnemyType):
        super().__init__()
        self.new_spd = 0
        self.new_x = 0
        self.new_y = 0
        self.type = enemy_type
        self.load_type()

    def reset(self):
        if self.type == EnemyType.OWL:
            self.new_x = 1500
            self.new_y = 303
        
        if self.type == EnemyType.SPIDER:
            self.new_x = 1300
            self.new_y = 400

    def load_type(self):
        if self.type == EnemyType.OWL:
            self.load_owl()
        if self.type == EnemyType.SPIDER:
            self.load_spider()

    def load_owl(self):
        self.image = VisualizationService.get_owl_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.new_x = random.randint(1500, 1900)
        self.new_y = 303
        self.new_spd = 5

    def load_spider(self):
        self.image = VisualizationService.get_spider_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.new_x = random.randint(900, 1200)
        self.new_y = 400
        self.new_spd = 7

    def move(self, scoreboard: ScoreBoard):
        self.new_x -= self.new_spd
        self.rect.midbottom = (self.new_x, self.new_y)

        if self.rect.right < 0:
            scoreboard.increase_score()

        if self.rect.right < 0:
            self.rect.left = Config.WIDTH

            if self.type == EnemyType.OWL:
                self.new_x = random.randint(1300, 1900)
                self.new_y = 303
            
            if self.type == EnemyType.SPIDER:
                self.new_x = random.randint(900, 1200)
                self.new_y = 400


    def draw(self, screen):
        screen.blit(self.image, self.rect)
