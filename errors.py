# Contains functions which can be used to handle errors

def err_with_sub(sub):
    """Handles an error where the question has a subject.""" 
    return f"sorry, i dunno anything about {sub}"

def err_without_sub():
    """Handles an error where the question has no subject."""
    return "sorry, i dunno."

## May not be needed
def err_unrelated():
    """Handles an error where the question is not for clarence."""
    return "i dunno, go look it up on google"

def err_unrelated_with_sub(sub):
    """Handles an error where the question is not for clarence and has a subject."""

def err_unrelated_without_sub():
    """Handles an error where the question is not for clarence and has no subject."""
    return "what are you even asking me about? is it that hard to look it up on google?"