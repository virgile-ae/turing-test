# Contains functions which can be used to handle errors
from random import choice


def err_without_sub():
    """Handles an error where the question has no subject."""
    return "i dunno, sry"


def err_with_sub(sub):
    """Handles an error where the question has a subject."""
    return f"i dunno anything about {sub}, sry"


def err_not_q():
    """Handles an error where there is no question."""
    not_q = ["is that even a question", "what are you trying to ask me?",
             "take a second to try and formulate what you're gonna say because that made absolutely no sense",
             "if you had a memory better than that of a goldfish, you would remember that you are supposed to ask me "
             "questions and not whatever you've just randomly spouted from your mouth"]
    return choice(not_q)
