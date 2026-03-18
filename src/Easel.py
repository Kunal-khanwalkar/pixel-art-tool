import pygame
from .Canvas import Canvas
from .Spritesheet import Spritesheet

class Easel:
    def __init__(self) -> None:
        self.surf: pygame.surface.Surface = None

        self.canvas = Canvas()
        self.spritesheet = Spritesheet()

    def resize(self, parent_surf: pygame.surface.Surface) -> None:
        self.surf = pygame.surface.Surface((2 * parent_surf.get_width() // 3, parent_surf.get_height()))
        self.canvas.resize(self.surf)
        self.spritesheet.resize(self.surf)

    def blit(self, parent_surf: pygame.surface.Surface, coordinates: tuple[int, int]) -> None:
        parent_surf.blit(self.surf, coordinates)

        self.canvas.blit(self.surf, (0,0))
        self.spritesheet.blit(self.surf, (0, self.canvas.surf.get_height()))
