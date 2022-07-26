from termios import VEOL
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

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def move(self, vel):
        self.y += vel
        self.x += vel

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img: pygame.surface.Surface = YELLOW_SPACE_SHIP
        self.laser_img: pygame.surface.Surface = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, BLUE_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }


    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel





def main() -> None:
    run: bool = True
    FPS: int = 60
    level: int = 1
    lives: int = 5
    main_font: pygame.font.Font = pygame.font.SysFont("comicsans", 50)

    enemies = []

    wave_length = 5

    enemy_vel = 2
    
    player_vel: int = 5

    player: Ship = Player(WIDTH//2, 650)

    clock: pygame.Clock = pygame.time.Clock()

    def redraw_window() -> None:
        WIN.blit(BG, (0,0))
        # draw text
        lives_label: pygame.surface.Surface = main_font.render(f"Lives: {lives}", True, (255,255,255))
        level_label: pygame.surface.Surface = main_font.render(f"Level: {level}", True, (255,255,255))
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))


        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 50), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys: Sequence[bool] = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x - player_vel > 0:
            player.x -= player_vel
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel 
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and player.y - player_vel > 0:
            player.y -= player_vel 
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel 

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)


        redraw_window()




if __name__ == "__main__":
    print(type(pygame.event.get()))
    main()

