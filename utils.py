from random import randint


def generate_random_number(min: int, max: int) -> int:
    """
    This function generates a random number between the min and max values

    :param min: The minimum number that can be generated
    :type min: int
    :param max: The maximum number that can be generated
    :type max: int
    :return: A random number between the min and max values.
    """
    return randint(min, max)
