import sys
import pygame

from src.Easel import Easel
from src.Palette import Palette

WIDTH: int = 800
HEIGHT: int = 600

class Painter:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Sprite Painter")
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        self.easel = Easel()
        self.palette = Palette()

        self._resize()

    def run(self) -> None:
        while True:
            self.easel.blit(self.surface, (0,0))
            self.palette.blit(self.surface, (self.easel.surf.get_width(), 0))

            self.easel.set_color(self.palette.get_color())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.WINDOWRESIZED:
                    self._resize()

            pygame.display.update()
            self.clock.tick(60)

    def _resize(self) -> None:
        self.easel.resize(self.surface)
        self.palette.resize(self.surface)

if __name__=='__main__':
    Painter().run()
