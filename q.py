# Contains the QType class
from enum import Enum


class QType(Enum):
    """Enumerates all different types of questions that could arise."""
    Fact = 0
    Opinion = 1
    Yes_No = 3
    Not_Q = 4
