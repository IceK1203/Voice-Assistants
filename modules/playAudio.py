import pygame
import os
import time
def play_audio(OUTPUT_FILE):

    pygame.init()
    pygame.mixer.music.load(OUTPUT_FILE)
    pygame.mixer.music.play()

    duration = pygame.mixer.Sound(OUTPUT_FILE).get_length()

    time.sleep(duration + 1)

    pygame.mixer.music.unload()
    os.remove(OUTPUT_FILE)