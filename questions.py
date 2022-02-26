# Contains functions to extract keywords which relate to:
# 		Who the question is for - your/you
#		What the question is about - jobs/interests/height
#		What type of question it is - who/what/when/do you/is
# Needs to be able to handle stuff like
#		Do you like - random yes or no
#		What do you think of - random i do(n't) like (thing) very much
# 		How is - random it is(n't) bad

from enum import Enum

class QType(Enum):
    Fact = 0
    Opinion = 1
    Unknown = 2
    Yes_No = 3

# Words which indicate that the question is for the bot (as opposed to general facts)
qs_for_bot = ["you", "your", "clarence", ]

fact_kws = ["can", "when", "who", "whose", "where", "when", "what", "does"]
opinion_kws = ["which"]
# might depend on whether it is personal or not
unknown_kws = [ "how", "what", "why"]
yes_no_kws = ["have", "did", "are"]

def is_directed_at_bot(question: list[str]) -> bool:
    """ Checks if the question is directed towards the bot or not.
    If it is the bot should either look up an answer or randomly generate one.
    If it isn't the bot should look it up on google."""
    for word in question:
        if word in qs_for_bot:
            return True
    return False


def type_of_q(question: list[str]) -> QType:
    """Finds all the possible types of question which QType might be"""
    do = False
    for i in question:
        t = i.strip()
        if t in fact_kws:
            return QType.Fact
        elif t in opinion_kws:
            return QType.Opinion
        elif t in unknown_kws:
            return QType.Unknown
        elif t in yes_no_kws:
            return QType.Yes_No    
        elif t in ["do", "doing", "done"] :
            do = True
    if do:
        return QType.Yes_No
    return None