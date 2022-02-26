# Contains functions which are used for the command prompt

# Introduces clarence
def intro():
	print("Hello, my name is Clarence Smith. Feel free to ask me any questions.")

# Excuses clarence
def outro():
	print("Well it's been nice, but I have to go. See ya later.")

# Asks the user what their next question is
def ask_question(n):
	print(f"You have {n} questions left.")
	return input("What is your question: ")
