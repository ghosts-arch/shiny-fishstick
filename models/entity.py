from utils import generate_random_number
from bars import hp_bar


# It's a class that represents an entity in a game
class Entity:
    def __init__(self, name: str) -> None:
        self._name = name
        self._life = generate_random_number(40, 50)
        self._MAX_LIFE_STAT = self._life
        self._shield = generate_random_number(0, 6)
        self._MAX_ATTACK_STAT = 6

    def get_name(self) -> str:
        return self._name

    def get_life(self) -> int:
        return self._life

    def get_unabsorbed_damages(self, dammages):
        infliged_dammages = dammages - self.get_shield()
        if infliged_dammages < 0:
            infliged_dammages = 0
        return infliged_dammages

    def set_life(self, dammages):
        self._life -= dammages

    def get_shield(self) -> int:
        return self._shield

    def attack(self):
        return generate_random_number(0, self._MAX_ATTACK_STAT)

    def defense(self, degats):
        return degats - self.get_shield()

    def display_stats(self) -> None:
        print(
            f"\n\t{self.get_name().title()}\n\t{hp_bar(self.get_life(), self._MAX_LIFE_STAT)} {self.get_life()}/{self._MAX_LIFE_STAT}\n\t{self.get_shield()} 🛡️\n")
