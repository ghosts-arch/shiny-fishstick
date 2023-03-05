from random import randint
from models.player import Player
from ennemy_generator import generate_ennemy

player_name = str(input("Nom du personnage : "))

player = Player(player_name)
player.display_stats()

ennemy = generate_ennemy(level=0)
ennemy.display_stats()

print(
    f"##### {ennemy.get_name()} (niveau {ennemy.get_level()}), Début du combat #####")
while (True):
    print("1. attaque")
    user_choice = int(input("> "))
    if user_choice == 1:
        player_attack = player.attack()
        ennemy_infliged_dammages = ennemy.get_unabsorbed_damages(player_attack)
        ennemy.set_life(ennemy_infliged_dammages)
        print(
            f"\tVous infliger {ennemy_infliged_dammages} dégats à {ennemy.get_name()}")
        ennemy.display_stats()

    if ennemy.get_life() <= 0:
        print(f"{player_name} à gagné !")
        break

    ennemy_attack = ennemy.attack()
    player_infliged_dammages = player.get_unabsorbed_damages(ennemy_attack)
    player.set_life(player_infliged_dammages)
    print(f"\t{ennemy.get_name()} vous inflige {player_infliged_dammages} dégats""")
    player.display_stats()

    if player.get_life() <= 0:
        print(f"{ennemy.get_name()} à gagné !")
        break

    if player.get_life() <= 0 and ennemy.get_life() <= 0:
        print("Egalité !")
        break

    print("\n\t##### tour suivant #####\n")
