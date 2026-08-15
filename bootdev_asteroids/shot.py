from typing import override

import pygame

from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SHOT_LIFESPAN,
    SHOT_RADIUS,
)


class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        self.lifespan = SHOT_LIFESPAN

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        # Move the shot
        self.position += self.velocity * dt

        # Wrap coordinates
        self.position.x = self.position.x % SCREEN_WIDTH
        self.position.y = self.position.y % SCREEN_HEIGHT

        # Decrement lifespan
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()  # Removes the sprite from all Pygame groups
