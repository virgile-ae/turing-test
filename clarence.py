# Contains the clarence object with everything about clarence and the synonyms for any of clarence's properties
# Also contains functions to handle fetching info about clarence and building a response from that info
from q import QType


# ***********************************************************
# CLASSES
# ***********************************************************


class Info:
    """Stores info about clarence and how to handle that info."""
    def __init__(self, d, nd, templ, negtempl, syn, aqt, aa=False):
        self.Detail = d
        self.NegativeDetail = nd
        self.Templates = templ
        self.NegativeTemplates = negtempl
        self.Synonyms = syn
        self.AcceptedQTypes = aqt
        self.AlreadyAsked = aa


# ***********************************************************
# VARIABLES
# ***********************************************************

being = ["i am _", "i happen to be _", "i am in fact, _"]

# TODO: add a 'expected qtype' field TODO: generate a random reply if qtype is incorrect TODO: *MORE IMPORTANT* add a
#  priority for keywords so adjectives and features (of people and objects have a lower priority than people and
#  objects
# Everything that you need to know about clarence
clarence = {
    # Name
    "name": Info("Clarence", "", ["my first name is _"], [], ["called"], [QType.Fact], True),
    "surname": Info("Smith", "", ["my surname is _"], [], [], [QType.Fact], True),
    # Job
    "job": Info("secretary", "", ["i work as a _ and i find it quite boring", "i have the very mundane job of _"], [],
                ["occupation", "work", "career"],
                [QType.Fact]),
    "income": Info("$68,500", "", ["i make _ a year"], [], ["money", "wealth", "cash", "dough"], []),
    # Age
    "age": Info("25", "", being, [], ["old"], []),
    "birthday": Info("6th May 1996", "", ["i was born on the _"], [], ["born"], []),
    # Country
    "home": Info("Melbourne, Australia", "", ["i live in _", "my current residence is in _"],
                 ["everywhere apart from Melbourne"], ["country", "from"],
                 [QType.Fact]),
    "ethnicity": Info("caucasian", "", being, [], ["race"], []),
    # Body
    "sexuality": Info("gay", "", being, [], ["gay", "lesbian", "lgbt", "lgbtqia", "lgbtq", "rainbows"], [QType.Fact]),
    "girlfriend": Info("", "", ["i'm gay", "did you just assume that i confine myself to the norm of heterosexuality. "
                                           "absolute fool."], [], ["bf"], []),
    "boyfriend": Info("", "", ["not yet", "hopefully soon", "why? are you open?"], [], ["bf"], []),
    "gender": Info("male", "", being, [], ["sex", "male", "female"], []),
    "height": Info("179cm", "", ["sadly, i am _ tall", "i am _ tall"], [], ["tall", "small"], []),
    "weight": Info("73kg", "", ["i weigh _", "i weigh a total of _"], [], ["heavy", "weigh", "mass"], []),
    # Hobbies
    "hobby": Info("hiking", "running", ["i enjoy _", "i like _"], ["_ is actually painful", "idk how anyone likes _"],
                  ["hobbies", "pastime", "pastimes", "thing", "things"], []),
    "subject": Info("art", "history", ["my favorite subject is _", "_ is best"],
                    ["_ sucks, it's just sooo boring", "_ should be a thing of the past"], ["lesson", "art", "class"],
                    []),
    # Sport
    "sport": Info("chess", "anything that increases my heart rate", ["my favorite sport is _", "i quite fancy _"],
                  ["i dislike with a passion _", "i hate _"], ["sports", "exercise"], []),
    # Mental well-being
    "feeling": Info("", "", ["i am feeling not that bad for once", "i feeling dead inside", "could be doing better",
                             "i wanna die, but not today at least"], [], ["doing"], []),
    # Color
    "color": Info("purple", "khaki green", ["my favorite color is by far _", "_, obviously"],
                  ["tbh, _ is so ugly", "_ is by far the worst"], ["colour", "shade", "tone"], []),
    # Pets and family
    "pet": Info("", "", ["i have no pets"], [], ["pets", "cat", "dog"], []),
    "family": Info("", "", ["i am an only child and my parents died in a car crash when i was two"], [],
                   ["brother", "sister", "siblings", "sisters", "brothers", "father", "mother", "grandfather",
                    "grandmother", "grandparents", "parents"], []),
    # Food
    "food": Info("pizza", "soup", ["my favorite food is _", "i don't mind a good _", "i couldn't live without _"],
                 ["i absolutely loathe _", "i think the world would be a better place without _"], ["eat", "ingest"],
                 []),
    # Media
    "film": Info("Star Wars: Empire Strikes Back", "Frozen 2",
                 ["my favorite movie is '_'", "the movie i like to watch most is _"],
                 ["i absolutely hate _", "my least favorite movie is by far, _"], ["movie", "cinema", "movies"], [],
                 False),
    "tv": Info("Big Bang Theory", "Riverdale", ["i like to watch _", "my favorite tv series is _"],
               ["my least favorite show is _", "i hated everything after season 2 of _"], ["show"], []),
    "music": Info("heavy metal", "blues", ["my favorite type of music is _"],
                  ["i don't understand how people can tolerate _"], ["listen", "genre"], []),
    "song": Info("", "", ["i love _ with a burning passion"], [], ["songs", "track", "tracks"], []),
    "book": Info("Alex Rider", "Jane Eyre", ["i have always loved _", "it has always been _"],
                 ["_ is the worst", "i can't stand _"], ["book", "novel", "novella"], []),
}

# All keywords
keywords = [
    *list(clarence.keys()),  # All the keys
    *[item for elems in list(clarence.values()) for item in elems.Synonyms]
]
