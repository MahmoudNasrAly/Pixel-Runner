import pygame

from src.services.visualization_service import VisualizationService
from src.config import Config


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = VisualizationService.get_palyer_image()
        self.rect = self.image.get_rect(midbottom=(70, 400))
        self.mask = pygame.mask.from_surface(self.image)
        self.gravity = 0
        self.speed = 3

    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.rect.bottom >= 400:
            self.gravity = -23
        if keys[pygame.K_RIGHT] and self.rect.right < Config.WIDTH:
            self.rect.x += 4
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 4
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
    
    def update(self):
        self.player_input()
        self.apply_gravity()

    def reset(self):
        self.rect.x = 70
        self.rect.y = 400
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
