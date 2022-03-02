# Contains the function which is to be looped over in main
import prompt
from questions import QType, type_of_q, parse_question, handle_fact, handle_opinion, handle_unknown, handle_yes_no
from keywords import find_keywords
from gpt3 import get_response_gpt3
from errors import err_unrelated_without_sub

def handle_q(i):
    """WHAT THIS SHOULD DO:
        Find type of question
        Find subject of question
        Find who the question is directed to
        Handle the question based on these parameters"""
    # Splits into words and checks if the question is for the bot
    question, for_bot = parse_question(prompt.ask_question(3-i).lower())
    # Finds the type of question
    type = type_of_q(question)
    # Find subject(s)
    subjects = find_keywords(question)
    if for_bot:
        if type == QType.Fact:
            pass
        elif type == QType.Opinion:
            pass
        elif type == QType.Unknown:
            print("none of them")
        elif type == QType.Yes_No:
            handle_yes_no(question)
        elif type == QType.Not_Q:
            pass
    else:
        # Fallback
        
        print("debugging: gpt3")
        if subjects != []:
            print(get_response_gpt3(" ".join(question)))
        else:
            print(err_unrelated_without_sub())