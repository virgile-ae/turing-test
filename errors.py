# Contains functions which can be used to handle errors

def err_without_sub():
    """Handles an error where the question has no subject."""
    return "i dunno, sry"

def err_with_sub(sub):
    """Handles an error where the question has a subject.""" 
    return f"i dunno anything about {sub}, sry"