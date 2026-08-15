import sys
from threading import currentThread

import pygame
from pygame.time import Clock

from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from constants import (
    ASTEROID_DAMAGE,
    INVUL_TIME,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    STARTING_HEALTH,
    STARTING_SCORE,
)
from hud import draw_hud
from logger import log_event, log_state
from on_hit import on_hit
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player_score: int = STARTING_SCORE
    player_health: int = STARTING_HEALTH
    invul_timer: float = INVUL_TIME
    asteroid_damage: int = ASTEROID_DAMAGE

    dt = 0.0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # --- Inside your main update/game loop ---

        # 1. If the player is currently invulnerable, just count down the timer
        if invul_timer > 0:
            invul_timer -= dt
            invul_timer = max(
                invul_timer, 0
            )  # Ensure it cleanly resets to 0 when finished

        # 2. If the player is NOT invulnerable, check for a fresh collision
        else:
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    # First collision detected! Trigger on_hit immediately
                    player_health, invul_timer = on_hit(player_health, asteroid_damage)
                    break  # Stop checking other asteroids this frame since we were hit

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        draw_hud(screen, player_score, player_health, invul_timer)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
