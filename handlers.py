# Contains the function which is to be looped over in main
from prompt import ask_question, ask_random_q, return_question, bot_speak
from gpt3 import get_response_gpt3
from enjoy import rand_bool, rand_opinion_on, rand_yes_no
from errors import err_not_q, err_without_sub
from text import find_keywords, sub_template, any_in, split_into_words, parse_subject_after, type_of_q, \
    is_directed_at_bot, is_negative
from q import QType
from clarence import clarence
from random import choice


# ***********************************************************
# HANDLERS
# ***********************************************************


def handle_yes_no(question):
    """Handles a yes or no question"""
    if "do" in question:
        kws = {
            "enjoy": ["like", "enjoy"],
            "own": ["have", "own"],
        }
        if any_in(kws["enjoy"], question):
            return rand_opinion_on(" ".join(parse_subject_after(kws["enjoy"], question)))
        elif any_in(kws["own"], question):
            subject = " ".join(parse_subject_after(kws["own"], question))
            if rand_bool():
                return f"yes i do have {subject}"
            else:
                return f"sadly, i don't have {subject}"
    elif any_in(["have", "will"], question):
        kws = ["been", "gone", "be", "go"]
        not_these = ["recently", "yesterday"]
        words = parse_subject_after(kws, question)
        words = " ".join(list(filter(lambda x: x not in not_these, words)))
        if rand_bool():
            return f"sadly, i haven't {words}"
        return f"funny you should say that. i {words} last weekend"
    else:
        return rand_yes_no()


# For repeat questions
again = ["you already know this, but nevertheless, ", "again?? *sigh*, ", "once again, ", "it hasn't changed; ",
         "try to exercise your memory a bit. as it seems you have forgotten, "]


def handle_sentence(sentence):
    """Generates a response from info about Clarence."""
    subjects = find_keywords(sentence)
    if not subjects:
        # To handle how are you
        if ("how" in sentence and "are" in sentence and "you" in sentence) or\
           ("are" in sentence and "you" in sentence and "well" in sentence):
            subjects = ["feeling"]
    if len(subjects) > 0:
        feature = clarence[subjects[0]]
        for i in subjects:
            if clarence[i].Priority.value > feature.Priority.value:
                feature = clarence[i]
        # Was too long so it was extracted into a variable
        negs = feature.NegativeTemplates
        is_neg = is_negative(sentence)
        templ = choice(feature.Templates) if not is_neg or len(negs) == 0 else choice(negs)
        # If it has already been asked then choose a template from 'again'
        generated = choice(again) if feature.AlreadyAsked else ""
        feature.AlreadyAsked = True
        if feature.Detail == "":
            return generated + templ
        elif is_neg:
            return sub_template(templ, feature.NegativeDetail)
        return generated + sub_template(templ, feature.Detail)
    qtype = type_of_q(sentence)
    if qtype == QType.Yes_No:
        return handle_yes_no(sentence)
    else:       # if qtype == QType.Fact:
        # TODO: could also be error with sub so could use parse_subject_after
        return err_without_sub()


def handle_q(name):
    """
    Find who the question is directed to.
    Find type of question.
    Find subject of question.
    Handle the question based on these parameters.
    """
    question = ask_question(name).lower()
    words = split_into_words(question)

    # Impossible to be a valid question if it is this short
    if len(words) < 3:
        return bot_speak(err_not_q())

    if is_directed_at_bot(words):
        generated = handle_sentence(words)
        bot_speak(generated)

        # Randomly ask back to the user from time to time
        if rand_bool() and rand_bool():
            return_question(name)
        elif rand_bool() and rand_bool():
            ask_random_q(name)
    else:
        # Fallback if question is not about clarence
        bot_speak(choice(["Lemme think.", "Gimme a sec."]))
        bot_speak(get_response_gpt3(" ".join(words)))
