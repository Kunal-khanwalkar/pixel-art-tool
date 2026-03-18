import pygame

class Canvas:
    def __init__(self) -> None:
        self.surf: pygame.surface.Surface = None

        self._tile_size: int = 0
        self._rects: list[pygame.rect.Rect] = []
        self._X_PADDING: int = 0
        self._Y_PADDING: int = 0

    def resize(self, parent_surf: pygame.surface.Surface) -> None:
        self.surf = pygame.surface.Surface((parent_surf.get_width(), 3 * parent_surf.get_height() // 4))
        self._tile_size = min(self.surf.get_width(), self.surf.get_height()) // 9
        self._define_canvas_rects()

    def blit(self, parent_surf: pygame.surface.Surface, coordinates: tuple[int, int]) -> None:
        parent_surf.blit(self.surf, coordinates)
        self.surf.fill((100,200,100))

        self._draw_canvas()

    def _draw_canvas(self) -> None:
        for i in range (8 * 8):
            pygame.draw.rect(self.surf, (0,0,0), self._rects[i])
            self._hover_and_select(i, (0,0))

    def _hover_and_select(self, idx: int, offset: tuple[int, int]) -> None:
        transformed_mouse = (pygame.mouse.get_pos()[0] - offset[0], pygame.mouse.get_pos()[1] - offset[1])

        if self._rects[idx].collidepoint(transformed_mouse):
            pygame.draw.rect(self.surf, pygame.Color(0,0,0), self._rects[idx], 3)
            pygame.draw.rect(self.surf, pygame.Color(255,255,255), self._rects[idx], 2)
            pygame.draw.rect(self.surf, pygame.Color(0,0,0), self._rects[idx], 1)

    def _define_canvas_rects(self) -> None:
        self._rects: list[pygame.rect.Rect] = []
        self._X_PADDING = (self.surf.get_width() - (self._tile_size * 8)) // 2
        self._Y_PADDING = (self.surf.get_height() - (self._tile_size * 8)) // 2

        for i in range(8 * 8):
            x = (i % 8) * self._tile_size + self._X_PADDING
            y = (i // 8) * self._tile_size + self._Y_PADDING
            self._rects.append(pygame.rect.Rect(x, y, self._tile_size, self._tile_size))