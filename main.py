import pygame
from pygame import mask
from pygame.sprite import Group, Sprite

from settings import size, height, load_image

pygame.init()
screen = pygame.display.set_mode(size)


class Mountain(Sprite):
    image = load_image("mountains.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = mask.from_surface(self.image)
        self.rect.bottom = height


class Landing(Sprite):
    image = load_image("pt.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = load_image('pt.png')
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


all_sprites = Group()
mountain = Mountain()
clock = pygame.time.Clock()
fps = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Landing(event.pos)
    screen.fill('aqua')
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
