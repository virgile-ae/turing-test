# Contains the clarence object with everything about clarence and the synonyms for any of clarence's properties
# Also contains functions to handle fetching info about clarence and building a response from that info
from dataclasses import dataclass
# from enjoy import rand_elem
# from template import handle_yes_no
# from errors import err_with_sub, err_without_sub


# ***********************************************************
# CLASSES
# ***********************************************************

class Info:
    """Stores info about clarence and how to handle that info."""
    def __init__(self, detail, templates, synonyms):
        self.Detail = detail
        self.Templates = templates
        self.Synonyms = synonyms

@dataclass(init=True)
class Synonym:
    """Stores required and optional words needed in a sentence for a synonym to be valid."""
    Required = ""
    Optional = []

# ***********************************************************
# VARIABLES
# ***********************************************************

being = ["i am _", "i happen to be _", "i am in fact, _"]

# Everything that you need to know about clarence
clarence = {
    # Name
    "name": Info("Clarence", ["my first name is _"], ["called"]),
    "surname": Info("Smith", ["my surname is _"], []),
    # Job
    "job": Info("secretary", ["i work as a _"], ["occupation", "work", "career"]),
    "income": Info("$68,500", ["i make _ a year"], ["money", "wealth", "cash", "dough"]),
    # Country
    "home": Info("Melbourne, Australia", ["i live in _", "my current residence is in _"], ["country", "from"]),	
    "ethnicity": Info("caucasian", being, ["race"]),
    # Body
    "sexuality": Info("gay", being, ["gay", "lgbt", "lgbtqia+", "lgbtq+", "rainbows"]),
    "gender": Info("male", being, ["sex", "male", "female"]),
    "height": Info("179cm", ["sadly, i am _ tall", "i am _ tall"], ["tall", "small"]),
    "weight": Info("73kg", ["i weigh _", "i weigh a total of _"], ["heavy", "weigh"]),
    # Age
    "age": Info("25", being, ["old"]),
    "birthday": Info("6th May 1996", ["i was born on the _"], ["born"]),
    # Hobbies
    "hobby": Info("hiking", ["i enjoy _", "i like _"], ["hobbies", "pastime", "pastimes"]),
    "subject" : Info("art", ["my favorite subject is _"], ["lesson", "art"]),
    # Sport
    "sport": Info("chess", ["my favorite sport is _", "i quite fancy _"], ["sports", "exercise"]),
    # Music
    "music": Info("heavy metal", ["my favorite type of music is _"], ["listen", "genre"]),
    # Mental wellbeing
    "feeling": Info("not bad", ["i am feeling _", "i am doing _"], ["doing"]),
    # Pets and family
    "pet": Info("", ["i have no pets"], ["pets", "cat", "dog"]),
    "family": Info("", ["i am an only child and my parents died in a car crash when i was two"], ["brother", "sister", "siblings", "sisters", "brothers", "father", "mother", "grandfather", "grandmother", "grandparents", "parents"]),
    # Food
    "food": Info("pizza", ["my favorite food is _", "i don't mind _"], ["eat", "ingest"]),
    # Movies and TV
    "film": Info("Star Wars: Empire Strikes Back", ["my favorite movie is '_'"], ["movie", "cinema", "movies"]),
    "tv" : Info("Big Bang Theory", ["i like to watch _"], ["show"]),
}

# All keywords
keywords = [
    *list(clarence.keys()), # All the keys
    *[item for elems in list(clarence.values()) for item in elems.Synonyms]
]
if tomato == "red":
    print("hello world")
