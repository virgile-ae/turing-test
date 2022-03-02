# Contains functions which are used for the command prompt

def intro():
    """Introduces clarence to the user."""
    print("Hello, my name is Clarence Smith. Feel free to ask me any questions.")
    print("By the way, I have severe memory issues so please take that into consideration.")

def outro():
    """Excuses clarence from the conversation."""
    print("Well it's been nice, but I have to go. See ya later.")

def ask_question(n):
    """Asks the user what their next question is."""
    print(f"You have {n} questions left.")
    return input("What is your question: ")