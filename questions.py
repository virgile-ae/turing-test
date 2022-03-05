# Contains functions to extract keywords which relate to:
# Needs to be able to handle stuff like
from re import findall
from enum import Enum
from enjoy import rand_opinion_on, rand_yes_no, parse_subject_after_any
import clarence

class QType(Enum):
    Fact = 0
    Opinion = 1
    Yes_No = 3
    Not_Q = 4

# Words which indicate that the question is for the bot (as opposed to general facts)
qs_for_bot = ["you", "your", "clarence", "yours"]

# Question keywords
fact_kws = ["can", "when", "who", "whose", "where", "when", "what", "does", "how", "what"]
opinion_kws = ["which", "think", "why"]
yes_no_kws = ["have", "did", "are", "do", "will", "is"]

def is_directed_at_bot(question):
    """ Checks if the question is directed towards the bot or not.
    If it is the bot should either look up an answer or randomly generate one.
    If it isn't the bot should look it up on google."""
    for word in question:
        if word in qs_for_bot:
            return True
    return False

def any_in(words, sentence):
    """Returns true if any of the words are in the sentence"""
    for word in words:
        if word in sentence:
            return True
    return False

def type_of_q(question):
    """Finds all the possible types of question which QType might be"""
    for i in question:
        t = i.strip()
        if t in fact_kws:
            return QType.Fact
        elif t in opinion_kws:
            return QType.Opinion
        elif t in yes_no_kws:
            return QType.Yes_No
    return QType.Not_Q

def parse_question(question):
    """Parses question, removing useless words and any punctuation."""
    # Splits into words, ignoring any punctuation
    words = list(findall(r"[\w']+", question))
    return words, is_directed_at_bot(words)

def handle_yes_no(question):
    """Handles a yes or no question"""
    enjoy = ["like", "enjoy"]
    if "do" in question:
        if any_in(enjoy, question):
            return rand_opinion_on(" ".join(parse_subject_after_any(enjoy, question)))

        elif any_in(["have", "own"], question):
            keywords = clarence.find_keywords(question)
            if clarence.clarence[keywords[[0]]]:
                return f"yes i do have a {clarence[keywords[0]]}"
            else:
                return f"sadly not"
    elif "have" in question or "will" in question:
        kws = ["been", "gone", "be", "go"]
        return rand_opinion_on(" ".join(parse_subject_after_any(kws, question)))
    else:
        return rand_yes_no()