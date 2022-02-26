# Contains things for dealing with keywords (excluding you/your)
from clarence import clarence

# Synonyms for different keywords
synonyms = {
    "name": ["called"],
    "job": ["occupation", "work", "career"],
    "income": ["money", "wealth"],
    "sexuality": ["gay", "lgbt", "lgbtqia+", "lgbtq+", "rainbows"],
    "gender": ["sex", "male", "female"],
    "height": ["tall", "small"],
    "weight": ["heavy", "weigh"],
    "date": ["when"],
    "birthday": ["born"],
    "sport": ["sports"],
    "music": ["listen", "genre"],
    "feeling": ["doing"],  # how are you doing?
}

_keywords_with_answer = list(clarence.keys())
_synonym_kws = [item for sublist in synonyms.values() for item in sublist]
keywords = [*_keywords_with_answer, *_synonym_kws]
