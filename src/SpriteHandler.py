class Sprite:
    def __init__(self, x, y, color) -> None:
        self.x: int = x
        self.y: int = y
        self.color: str = color

class SpriteHandler:
    def __init__(self) -> None:
        self.sprites: list[Sprite] = [Sprite(i % 128, i // 128, "#000000") for i in range(128 * 32)]
        self.offset: int = 0 # selected tile

    def save(self, filename: str) -> None:
        with open(filename, 'w') as f:
            for sprite in self.sprites:
                f.write(f"{sprite.x},{sprite.y},{sprite.color}\n")