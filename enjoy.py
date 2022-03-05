# Contains functions to handle questions about enjoyment
from random import getrandbits, randint, choice


# ***********************************************************
# RANDOM STUFF (literally) for things not in clarence object
# ***********************************************************

def rand_bool():
    """Returns a random bool which can be used to make decisions about whether or not clarence enjoys something."""
    return not getrandbits(1)


def rand_elem(elems):
    """Returns a random element from a list."""
    index = randint(0, len(elems) - 1)
    return elems[index]


# TODO: templates for rand_opinion_on
def rand_opinion_on(kw):
    """Generates a response about question asking about an opinion on something."""
    if rand_bool():
        return f"to be perfectly honest, i don't really like {kw}, so nah"
    return f"i actually quite like {kw}, so yeh"


# ***********************************************************
# FIND RESPONSE
# ***********************************************************

yes = ["yep", "yes", "totally", "kinda", "maybe"]
no = ["nah", "not really", "very little", "don't remember"]


def rand_yes_no():
    """Random reply to a yes-no question."""
    if rand_bool():
        return choice(yes)
    return choice(no)
