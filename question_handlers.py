import clarence
from enjoy import rand_opinion_on, rand_yes_no, parse_subject_after_any
from questions import any_in

def handle_yes_no(question):
    """Handles a yes or no question"""
    if "do" in question:

        if any_in(["like", "enjoy"], question):
            kws = ["enjoy", "like"]
            print(rand_opinion_on(" ".join(parse_subject_after_any(kws, question))))

        elif any_in(["have", "own"], question):
            keywords = clarence.find_keywords(question)
            if clarence.clarence[keywords[[0]]]:
                print(f"yes i do have a {clarence[keywords[0]]}")
            else:
                print(f"sadly not")
    elif "have" in question or "will" in question:
        kws = ["been", "gone", "be", "go"]
        print(rand_opinion_on(" ".join(parse_subject_after_any(kws, question))))
    else:
        print(rand_yes_no())