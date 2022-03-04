# Contains the function which is to be looped over in main
import prompt
from questions import parse_question
from template import handle_sentence
from gpt3 import get_response_gpt3
from enjoy import rand_bool, rand_elem
from errors import err_not_q


def handle_q(name):
    """
    Find who the question is directed to.
    Find type of question.
    Find subject of question.
    Handle the question based on these parameters.
    """
    # Splits into words and checks if the question is for the bot
    question, for_bot = parse_question(prompt.ask_question(name).lower())
    print("Clarence: ", end="")

    # Impossible to be a valid question if this short
    if len(question) < 3:
        return print(err_not_q())

    if for_bot:
        print(handle_sentence(question))
        ## Check if subject can be handled
        ## Else fallback on errors or generic reply
        if rand_bool() and rand_bool():
            prompt.return_question()
    else:
        # Fallback if question is not about clarence
        print("Lemme think.")
        print(get_response_gpt3(" ".join(question)))
    
