from .entity import Entity


class Ennemy(Entity):
    def __init__(self, name: str, level: int = 0) -> None:
        super().__init__(name)
        self._level = level

    def get_level(self):
        return self._level
