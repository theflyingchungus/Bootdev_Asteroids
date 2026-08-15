import pygame

pygame.font.init()
hud_font = pygame.font.Font(None, 32)


def draw_hud(screen: pygame.Surface, score: int, health: int, i_frame: float):
    score_text = hud_font.render(f"Score: {score}", True, "white")
    health_text = hud_font.render(f"Health: {health}", True, "white")
    invul_text = hud_font.render(f"i-frame: {round(i_frame, 2)}", True, "white")

    screen.blit(score_text, (20, 20))
    screen.blit(health_text, (20, 55))
    screen.blit(invul_text, (20, 90))
