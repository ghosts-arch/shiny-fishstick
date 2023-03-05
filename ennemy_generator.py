from models.ennemy import Ennemy
from random import choice


def generate_ennemy(level: int = 0) -> Ennemy:
    ennemies_names = ["dragon", "chevalier", "gargouille"]
    name = choice(ennemies_names)
    return Ennemy(name, level)
