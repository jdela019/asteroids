# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# imports constants
from constants import *

def main():
  pygame.init()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  # Game loop
  while True:
    # Allows user to exit
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return

    # Makes screen black
    pygame.Surface.fill(screen, (0,0,0))

    # Refreshes screen
    pygame.display.flip()


if __name__ == "__main__":
    main()