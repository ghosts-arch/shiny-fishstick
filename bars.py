def hp_bar(hp, max_hp):
    """
    It takes the current hp and max hp and returns a string of red and white blocks that represents the
    current hp as a percentage of the max hp

    :param hp: The current health of the player
    :param max_hp: The maximum amount of health the player can have
    :return: a string.
    """
    return f"\x1b[91m{'■'* int(((hp * 100) / max_hp)/10)}\x1b[0m{'■' * int(10 - int(((hp * 100) / max_hp)/10))}"
