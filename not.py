# Need to handle negative words
# no, not , don't, never, least, 
from questions import any_in

def check_negative(sentence):
    """Checks if the question is looking for an opinion on a negative subject."""
    return any_in(sentence)
