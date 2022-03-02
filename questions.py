# Contains functions to extract keywords which relate to:
# 		Who the question is for - your/you
#		What the question is about - jobs/interests/height
#		What type of question it is - who/what/when/do you/is
# Needs to be able to handle stuff like
#		Do you like - random yes or no
#		What do you think of - random i do(n't) like (thing) very much
# 		How is - random it is(n't) bad
from re import findall
from enum import Enum
from enjoy import rand_opinion_on, rand_yes_no, parse_subject_after_any, rand_elem
from clarence import clarence, find_keywords

class QType(Enum):
    Fact = 0
    Opinion = 1
    Yes_No = 3
    Not_Q = 4


# Words which indicate that the question is for the bot (as opposed to general facts)
qs_for_bot = ["you", "your", "clarence", "yours"]

fact_kws = ["can", "when", "who", "whose", "where", "when", "what", "does", "how", "what"]
opinion_kws = ["which", "think", "why"]
# might depend on whether it is personal or not
yes_no_kws = ["have", "did", "are", "do", "will", "is"]


def any_in(words, sentence):
    """Returns true if any of the words are in the sentence"""
    for word in words:
        if word in sentence:
            return True
    return False


def is_directed_at_bot(question):
    """ Checks if the question is directed towards the bot or not.
    If it is the bot should either look up an answer or randomly generate one.
    If it isn't the bot should look it up on google."""
    for word in question:
        if word in qs_for_bot:
            return True
    return False


def type_of_q(question):
    """Finds all the possible types of question which QType might be"""
    do = False
    for i in question:
        t = i.strip()
        if t in fact_kws:
            return QType.Fact
        elif t in opinion_kws:
            return QType.Opinion
        elif t in yes_no_kws:
            return QType.Yes_No
        elif t in ["do", "doing", "done"]:
            do = True
    if do:
        return QType.Yes_No
    return QType.Not_Q


def parse_question(question):
    """Parses question, removing useless words and any punctuation."""
    # Splits into words, ignoring any punctuation
    words = list(findall(r"[\w']+", question))
    return words, is_directed_at_bot(words)


def handle_yes_no(question):
    """Handles a yes or no question"""
    if "do" in question:

        if any_in(["like", "enjoy"], question):
            kws = ["enjoy", "like"]
            print(rand_opinion_on(" ".join(parse_subject_after_any(kws, question))))

        elif any_in(["have", "own"], question):
            keywords = find_keywords(question)
            if clarence[keywords[[0]]]:
                print(f"yes i do have a {clarence[keywords[0]]}")
            else:
                print(f"sadly not")
    elif "have" in question or "will" in question:
        kws = ["been", "gone", "be", "go"]
        print(rand_opinion_on(" ".join(parse_subject_after_any(kws, question))))
    else:
        print(rand_yes_no())

def handle_opinion():
    opinions = ["i don't really know to be honest", "maybe", "i'm not quite sure"]
    return rand_elem(opinions)
