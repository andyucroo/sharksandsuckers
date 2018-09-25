import time

import pygame

from niche import Niche
from games import prisonersDilemma
from players import Shark, Sucker


if __name__ == "__main__":
    screen = pygame.display.set_mode((960, 720))
    pygame.display.set_caption("Any key to quit")
    n = Niche()

    # Example 1
    n.fill((Shark(),),)
    n.fill((Sucker(), ), range(8, 12), range(9, 11))

    # Example 2
    #n.fill((Shark(),),)
    #n.fill((Sucker(), ), range(8, 12), range(5, 7))
    #n.fill((Sucker(),), range(8, 12), range(14, 16))

    n.rectangleDiagram(screen)
    while True:
        n = n.play(prisonersDilemma, 30)
        n.nextNiche = Niche(width = n.width, height=n.height, projection=False)
        n.rectangleDiagram(screen)
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) or (event.type == pygame.QUIT):
                exit()
        time.sleep(0.25)