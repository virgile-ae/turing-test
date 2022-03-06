# Contains the clarence object with everything about clarence and the synonyms for any of clarence's properties
# Also contains functions to handle fetching info about clarence and building a response from that info
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from q import QType

# To reply to questions about time
now = datetime.now()


# ***********************************************************
# CLASSES
# ***********************************************************
class Priority(Enum):
    """Priority of different keywords"""
    About = 1
    Object = 2


@dataclass()
class Info:
    """Stores info about clarence and how to handle that info."""
    Detail: str
    NegativeDetail: str
    Templates: list[str]
    NegativeTemplates: list[str]
    Synonyms: list[str]
    AcceptedQTypes: list[QType]
    Priority: Priority
    AlreadyAsked: bool = False


# ***********************************************************
# VARIABLES
# ***********************************************************

being = ["i am _", "i happen to be _", "i am in fact, _"]

# TODO: add a 'expected qtype' field
# TODO: generate a random reply if qtype is incorrect
# Everything that you need to know about clarence
clarence = {
    # Name
    "name": Info("Clarence", "", ["my first name is _"], [], ["called"], [QType.Fact], Priority.Object, True),
    "surname": Info("Smith", "", ["my surname is _"], [], [], [QType.Fact], Priority.Object, True),
    # Job
    "job": Info("secretary", "", ["i work as a _ and i find it quite boring", "i have the very mundane job of _"], [],
                ["occupation", "work", "career"],
                [QType.Fact], Priority.About),
    "income": Info("$68,500", "", ["i make _ a year"], [], ["money", "wealth", "cash", "dough"], [], Priority.About),
    # Age
    "age": Info("25", "", being, [], ["old"], [], Priority.About),
    "birthday": Info("6th May 1996", "", ["i was born on the _"], [], ["born"], [], Priority.About),
    # Country
    "home": Info("Melbourne, Australia", "", ["i live in _", "my current residence is in _"],
                 ["everywhere apart from Melbourne"], ["country", "from"],
                 [QType.Fact], Priority.About),
    "ethnicity": Info("caucasian", "", being, [], ["race"], [], Priority.About),
    # Body
    "sexuality": Info("gay", "", being, [], ["gay", "lesbian", "lgbt", "lgbtqia", "lgbtq", "rainbows"], [QType.Fact],
                      Priority.About),
    "girlfriend": Info("", "", ["i'm gay", "did you just assume that i confine myself to the norm of heterosexuality. "
                                           "absolute fool."], [], ["bf"], [], Priority.Object),
    "boyfriend": Info("", "", ["not yet", "hopefully soon", "why? are you open?"], [], ["bf"], [], Priority.Object),
    "gender": Info("male", "", being, [], ["sex", "male", "female"], [], Priority.About),
    "height": Info("179cm", "", ["sadly, i am _ tall", "i am _ tall"], [], ["tall", "small"], [], Priority.About),
    "weight": Info("73kg", "", ["i weigh _", "i weigh a total of _"], [], ["heavy", "weigh", "mass"], [],
                   Priority.About),
    # Hobbies
    "hobby": Info("hiking", "running", ["i enjoy _", "i like _"], ["_ is actually painful", "idk how anyone likes _"],
                  ["hobbies", "pastime", "pastimes", "thing", "things"], [], Priority.About),
    "subject": Info("art", "history", ["my favorite subject is _", "_ is best"],
                    ["_ sucks, it's just sooo boring", "_ should be a thing of the past"], ["lesson", "art", "class"],
                    [], Priority.About),
    # Sport
    "sport": Info("chess", "anything that increases my heart rate", ["my favorite sport is _", "i quite fancy _"],
                  ["i dislike with a passion _", "i hate _"], ["sports", "exercise"], [], Priority.About),
    # Mental well-being
    "feeling": Info("", "", ["i am feeling not that bad for once", "i feeling dead inside", "could be doing better",
                             "i wanna die, but not today at least"], [], ["doing"], [], Priority.About),
    # Color
    "color": Info("purple", "khaki green", ["my favorite color is by far _", "_, obviously"],
                  ["tbh, _ is so ugly", "_ is by far the worst"], ["colour", "shade", "tone"], [], Priority.About),
    # Pets and family
    "pet": Info("", "", ["i have no pets"], [], ["pets", "cat", "dog"], [], Priority.Object),
    "family": Info("", "", ["i am an only child and my parents died in a car crash when i was two"], [],
                   ["brother", "sister", "siblings", "sisters", "brothers", "father", "mother", "grandfather",
                    "grandmother", "grandparents", "parents", "mom", "mum", "mummy", "dad", "daddy", "bro", "sis"], [],
                   Priority.Object),
    # Food
    "food": Info("pizza", "soup", ["my favorite food is _", "i don't mind a good _", "i couldn't live without _"],
                 ["i absolutely loathe _", "i think the world would be a better place without _"],
                 ["eat", "ingest", "pizza"],
                 [], Priority.About),
    # Media
    "film": Info("Star Wars: Empire Strikes Back", "Frozen 2",
                 ["my favorite movie is '_'", "the movie i like to watch most is _"],
                 ["i absolutely hate _", "my least favorite movie is by far, _"], ["movie", "cinema", "movies"], [],
                 Priority.About),
    "tv": Info("Big Bang Theory", "Riverdale", ["i like to watch _", "my favorite tv series is _"],
               ["my least favorite show is _", "i hated everything after season 2 of _"], ["show"], [], Priority.About),
    "music": Info("heavy metal", "blues", ["my favorite type of music is _"],
                  ["i don't understand how people can tolerate _"], ["listen", "genre"], [], Priority.About),
    "song": Info("", "", ["i love _ with a burning passion"], [], ["songs", "track", "tracks"], [], Priority.About),
    "book": Info("Alex Rider", "Jane Eyre", ["i have always loved _", "it has always been _"],
                 ["_ is the worst", "i can't stand _"], ["book", "novel", "novella"], [], Priority.About),
    # Time
    "time": Info(now.strftime("%H:%M"), "", ["last time i checked it was _"], [], ["hour"], [], Priority.Object)
}

# All keywords
keywords = [
    *list(clarence.keys()),  # All the keys
    *[item for elems in list(clarence.values()) for item in elems.Synonyms]
]
