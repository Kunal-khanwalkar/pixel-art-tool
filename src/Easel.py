import pygame
from .Canvas import Canvas
from .Spritesheet import Spritesheet

class Easel:
    def __init__(self) -> None:
        self.surf: pygame.surface.Surface = None

    def resize(self, parent_surf: pygame.surface.Surface) -> None:
        self.surf = pygame.surface.Surface((2 * parent_surf.get_width() // 3, parent_surf.get_height()))

    def blit(self, parent_surf: pygame.surface.Surface, coordinates: tuple[int, int]):
        parent_surf.blit(self.surf, coordinates)
        self.surf.fill((150,150,150))