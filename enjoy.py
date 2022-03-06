# Contains functions to handle questions about enjoyment
from random import getrandbits, randint, choice
from text import sub_template


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


def rand_opinion_on(kw):
    """Generates a response about question asking about an opinion on something."""
    like = ["i actually quite like _, so yeh", "i am a big fan of _"]
    dislike = ["to be perfectly honest, i don't really like _, so nah", "surprisingly, i hate _"]
    if rand_bool():
        return sub_template(choice(like), kw)
    return sub_template(choice(dislike), kw)


yes = ["yep", "yes", "totally", "kinda", "maybe"]
no = ["nah", "not really", "very little", "don't remember"]


def rand_yes_no():
    """Random reply to a yes-no question."""
    if rand_bool():
        return choice(yes)
    return choice(no)
