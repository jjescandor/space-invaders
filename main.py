from tkinter import W
import pygame
import os
import time
import random
import typing
from typing import List, Dict, Sequence

WIDTH, HEIGHT = 750, 750
WIN: pygame.surface.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
pygame.font.init()

# Load imaages

RED_SPACE_SHIP: pygame.surface.Surface = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP: pygame.surface.Surface = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP: pygame.surface.Surface = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
# Player Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER: pygame.surface.Surface = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER: pygame.surface.Surface = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER: pygame.surface.Surface = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
YELLOW_LASER: pygame.surface.Surface = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BG: pygame.surface.Surface = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))
class Ship():
    def __init__(self, x, y, health=100) -> None:
        self.x: int = x
        self.y: int = y
        self.health: int = health
        self.ship_img = None
        self.laser_img = None
        self.lasers: List[int] = []
        self.cool_down_count: int= 0
    
    def draw(self, window) -> None:
        window.blit(self.ship_img, (self.x, self.y))
        # pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50), 0)

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER

def main() -> None:
    run: bool = True
    FPS: int = 60
    level: int = 1
    lives: int = 5
    main_font: pygame.font.Font = pygame.font.SysFont("comicsans", 50)
    
    player_vel: int = 5

    ship: Ship = Ship(WIDTH//2, 650)
    clock: pygame.Clock = pygame.time.Clock()

    def redraw_window() -> None:
        WIN.blit(BG, (0,0))
        # draw text
        lives_label: pygame.surface.Surface = main_font.render(f"Lives: {level}", True, (255,255,255))
        level_label: pygame.surface.Surface = main_font.render(f"Level: {level}", True, (255,255,255))
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        ship.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys: Sequence[bool] = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and ship.x - player_vel > 0:
            ship.x -= player_vel
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and ship.x + player_vel + 50 < WIDTH:
            ship.x += player_vel 
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and ship.y - player_vel > 0:
            ship.y -= player_vel 
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and ship.y + player_vel + 50 < HEIGHT:
            ship.y += player_vel 




if __name__ == "__main__":
    print(type(pygame.event.get()))
    main()

