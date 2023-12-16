from dataclasses import dataclass
import enum
from typing import List  # TODO: can remove >= 3.9


# 1. make a BiteLevel enum class
# keys = INTRO BEGINNER INTERMEDIATE ADVANCED
# values = 1 2 3 4
# make sure they can be sorted by int value

class BiteLevel ...


# 2. make a dataclass that can be ordered
# attributes: number (int), title (str), level (BiteLevel)

class Bite ...


# 3. complete the function below

def create_bites(numbers: List[int], titles: List[str],
                 levels: List[BiteLevel]):
    """Generate a generator of Bite dataclass objects"""
    pass