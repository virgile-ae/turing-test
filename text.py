# Contains functions for processing text
from clarence import keywords, clarence
from re import findall
from q import QType


# ***********************************************************
# SENTENCES
# ***********************************************************


def split_into_words(question):
    """Splits a sentence into words, ignoring any punctuation."""
    words = list(findall(r"[\w']+", question))
    return words


def any_in(words, sentence):
    """Checks if any of the words are in the sentence."""
    for word in words:
        if word in sentence:
            return True
    return False


def parse_subject_after(kws, words):
    """Finds the subject after a certain keyword."""
    index = 0
    for i in kws:
        if i in words:
            try:
                index = words.index(i) + 1
            except:
                pass
    return words[index:]


# ***********************************************************
# TEMPLATING
# ***********************************************************

def sub_template(template, info) -> str:
    """Substitute the _ in the template with the info"""
    return template.replace("_", info)


# ***********************************************************
# KEYWORDS
# ***********************************************************

def is_keyword(word):
    """Checks if a word is a keyword."""
    return word in keywords


def synonym_for(kw):
    """Takes a word and checks if it is a keyword.
    Returns the word that it is a synonym for and a bool indicating success."""
    for k, v in clarence.items():
        if kw == k or kw in v.Synonyms:
            return k
    return ""


def find_keywords(sentence):
    """Returns all the keywords in a sentence."""
    kws = []
    for word in sentence:
        if not is_keyword(word):
            continue
        if word in clarence.keys():
            kws.append(word)
        else:
            kws.append(synonym_for(word))
    return kws


# ***********************************************************
# QUESTIONS
# ***********************************************************


# Words which indicate that the question is for the bot (as opposed to general facts)
qs_for_bot = ["you", "your", "clarence", "yours"]

# Question keywords
fact_kws = ["can", "when", "who", "whose", "where", "when", "what", "does", "how", "what"]
opinion_kws = ["which", "think", "why"]
yes_no_kws = ["have", "did", "are", "do", "will", "is"]


def is_directed_at_bot(question):
    """ Checks if the question is directed towards the bot or not.
    If it is the bot should either look up an answer or randomly generate one.
    If it isn't the bot should look it up on Google."""
    for word in question:
        if word in qs_for_bot:
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


# ***********************************************************
# NEGATIVE WORDS
# ***********************************************************

neg_words = ["no", "not", "never", "don't", "least"]


def is_negative(sentence):
    """Checks if the question is looking for an opinion on a negative subject."""
    return any_in(neg_words, sentence)
