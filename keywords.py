# Contains things for dealing with keywords (excluding you/your)
from clarence import clarence

# Synonyms for different keywords
synonyms = {
    "name": ["called"],
    "job": ["occupation", "work", "career"],
    "income": ["money", "wealth", "cash", "dough"],
    "sexuality": ["gay", "lgbt", "lgbtqia+", "lgbtq+", "rainbows"],
    "gender": ["sex", "male", "female"],
    "height": ["tall", "small"],
    "weight": ["heavy", "weigh"],
    "date": ["when"],
    "birthday": ["born"],
    "sport": ["sports"],
    "music": ["listen", "genre"],
    "feeling": ["doing"],  # how are you doing?
    "subject": ["lesson","art"],
    "food" : ["eat"],
    "film" : ["movie","cinema"],
    "tv": ["show"],
  
}

# Don't use outside of this file
_keywords_with_answer = list(clarence.keys())
_synonym_kws = [item for sublist in synonyms.values() for item in sublist]
# All keywords
keywords = [*_keywords_with_answer, *_synonym_kws]

def is_keyword(word):
    """Checks if a word is a keyword."""
    return word in keywords

def synonym_for(kw):
    """Takes a word and checks if it is a keyword. Returns the word that it is a synonym for and a bool indicating success."""
    for k, v in synonyms.items():
        if kw == k or kw in v:
            return k
    return ""
def is_main_kw(word):
    """Checks if a word is in the main keywords."""
    return word in list(synonyms.keys())

def find_keywords(sentence):
    """Returns all the keywords in a sentence."""
    kws = []
    for word in sentence:
        if not is_keyword(word):
            continue
        if is_main_kw(word):
            kws.append(word)
        else:
            kws.append(synonym_for(word))
    return kws