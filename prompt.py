# Contains functions which are used for the command prompt
from enjoy import rand_elem

def intro():
    """Introduces clarence to the user."""
    print("Hello, my name is Clarence Smith. Feel free to ask me any questions.")
    print("By the way, I have severe short term memory issues so please take that into consideration when conversing with me.")
    name = input("What is your name: ")
    print(f"Well {name}, feel free to ask me any questions.")
    return name

def outro():
    """Excuses clarence from the conversation."""
    print("Well it's been nice, but I have to go. See ya later.")

def ask_question(name):
    """Asks the user what their next question is."""
    return input(f"{name} (aka you the user): ")

questions = ["what about you", "and you", "hbu"]
replies = ["cool", "nice", "pog", "lol", "*audible laughter*", "oh well", "as if anyone cared", "*awkward stare*"]

def return_question():
    """Bounces back the question to the user."""
    input(rand_elem(questions) + "?\nEnter reply: ")
    print(rand_elem(replies))