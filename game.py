#Project by : Tina Amini,Zahra Ghasemi,Hasti Rezaiee :)
import pygame
import pygame as pg
import sys
import random
  #VARIABLES
display_width = 576
display_height = 1024
# START PYGAME MODULES
pygame.init()
main_screen = pygame.display.set_mode ((576, 1024))
clock = pygame.time.Clock
while True:
     for event in pygame.event.get()
       if event.type == pygame.Quit:
          pygame.quit()
          sys.exit()

      pygame.display.update()
      clock.tick(90)

