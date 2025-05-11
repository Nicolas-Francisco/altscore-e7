import random
from models.systems import SYSTEMS


def get_system_bay(system: str):
    return SYSTEMS[system]


def get_random_system():
    return random.choice(list(SYSTEMS.keys()))
