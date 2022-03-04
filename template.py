from clarence import keywords, clarence
from errors import err_without_sub
from questions import type_of_q, QType, handle_yes_no
from enjoy import rand_elem

# ***********************************************************
# TEMPLATING
# ***********************************************************

def sub_template(template: str, info):
    """Substitute the _ in the template with the info"""
    index = template.index("_")
    replaced = template[:index] + info + template[index+1:]
    return replaced

def handle_sentence(sentence):
    """Generates a response from info about clarence"""
    subjects = find_keywords(sentence)
    if len(subjects) > 0:
        feature = clarence[subjects[0]]
        templ = rand_elem(feature.Templates)
        if feature.Detail == "":
            return templ
        return sub_template(templ, feature.Detail)
    else:
        type = type_of_q(sentence)
        if type == QType.Fact:
            print(err_without_sub())
        elif type == QType.Yes_No:
            handle_yes_no()


# ***********************************************************
# KEYWORDS
# ***********************************************************

def is_keyword(word):
    """Checks if a word is a keyword."""
    return word in keywords

def synonym_for(kw):
    """Takes a word and checks if it is a keyword. Returns the word that it is a synonym for and a bool indicating success."""
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