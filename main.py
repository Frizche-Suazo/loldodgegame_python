import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dodge Game by Frizche Suazo")
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 200))
test_surface.fill("red")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (350, 200))
    pygame.display.update()

    clock.tick(60)
