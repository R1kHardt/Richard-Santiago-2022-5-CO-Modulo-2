import pygame

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import Large_Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = [SMALL_CACTUS,LARGE_CACTUS,BIRD]

    def update(self, game):
        if len(self.obstacles) == (0, 2) == 0:
            cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)
        elif len(self.obstacles) == (0, 2) == 1:
            cactus = Large_Cactus(LARGE_CACTUS)
            self.obstacles.append.update(cactus)  
        elif len(self.obstacles) == (0, 2) == 2:
            bird = Bird(BIRD)
            self.obstacles.append(bird)    

        for obstacle in self.obstacles:
          obstacle.update(game.game_speed, self.obstacles)
          if game.player.dino_rect.colliderect(obstacle.rect):
            pygame.time.delay(1000)
            game.playing = False
            break



    def draw(self,screen):
        for obstacle in self.obstacles:
          obstacle.draw(screen)
          