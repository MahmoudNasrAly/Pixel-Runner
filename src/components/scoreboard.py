from src.services.visualization_service import VisualizationService
from src.services.score_service import ScoreService
from src.config import Config


class ScoreBoard:

    def __init__(self):

        self._current_score = 0
        self._max_score = ScoreService.get_max_score()

    def reset(self):
        self._current_score = 0

    def increase_score(self):
        self._current_score += 1

    def get_max_score(self):
        return self._max_score

    def get_current_score(self):
        return self._current_score

    def update_max_score(self):
        if self._current_score > self._max_score:
            ScoreService.update_max_score(self._current_score)
            self._max_score = self._current_score

    def draw(self, screen):
        score_font = VisualizationService.get_score_font()
        score_text = score_font.render(
            f"Score: {self._current_score}", False, "Black")
        score_rect = score_text.get_rect(center=(Config.WIDTH // 2, 50))
        screen.blit(score_text, score_rect)
