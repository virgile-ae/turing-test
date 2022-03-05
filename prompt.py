# Contains functions which are used for the command prompt
from random import choice, randint
from enjoy import rand_elem


# **************************************************************
# INTRO AND OUTRO
# **************************************************************


def intro():
    """Introduces clarence to the user. Returns the name of the user"""
    sentence = "\n".join(["hello, my name is clarence smith. feel free to ask me any questions.",
                          "by the way, i have severe short term memory issues so please take that into consideration "
                          "when conversing with me."])
    bot_speak(sentence)
    name = input("Clarence: what is your name?\nUser: ")
    bot_speak(f"well {name}, feel free to ask me any questions.")
    return name


def outro():
    """Excuses clarence from the conversation."""
    bot_speak("Well it's been nice, but I have to go. See ya later.")


# **************************************************************
# OUTPUT TO CONSOLE
# **************************************************************


def bot_speak(sentence):
    """Formats and outputs sentence."""
    print(f"Clarence: {sentence}")


def ask_question(name):
    """Asks the user what their next question is. Returns the question."""
    return input(f"{name}: ")


# **************************************************************
# ASKING QUESTIONS
# **************************************************************

questions = ["what about you", "and you", "hbu"]
replies = ["cool", "nice", "pog", "lol", "*audible laughter*", "oh well", "as if anyone cared", "*awkward stare*",
           "sure", "hmmm", "*awkward silence*", "oh. anyways..."]


# TODO: use return_question and ask_random_q in handle_q
def return_question(name):
    """Bounces back the question to the user."""
    bot_speak(choice(questions))
    ask_question(name)
    bot_speak(choice(replies))


def ask_random_q(name):
    """Asks a random question."""
    whatQ = ["name", "favourite colour", "favourite film", "favourite tv show"]
    likeQ = ["star wars", "heavy metal", "the big bang theory"]
    howQ = ["old are you", "are you doing today", "is the weather where you live"]
    randNum = randint(1, 3)
    if randNum == 1:
        bot_speak(f"what is your {rand_elem(whatQ)}?")
    elif randNum == 2:
        bot_speak(f"do you like {rand_elem(likeQ)}?")
    else:
        bot_speak(f"how {rand_elem(howQ)}?")
    ask_question(name)
    bot_speak(choice(replies))
