import pygame

shoot_sound = None
break_sound = None


def init_sounds():
    global shoot_sound, break_sound
    shoot_sound = pygame.mixer.Sound("laser.mp3")
    break_sound = pygame.mixer.Sound("snare.mp3")

    # Optional: adjust volume (from 0.0 to 1.0)
    shoot_sound.set_volume(0.5)
    break_sound.set_volume(0.7)
