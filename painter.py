import sys
import pygame

WIDTH: int = 800
HEIGHT: int = 600

class Painter:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Sprite Painter")
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60)

if __name__=='__main__':
    Painter().run()
