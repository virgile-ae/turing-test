# Turing Test
# List who is in the group or if you are working alone.
# Shaurya and Virgile
import prompt
import keywords
from questions import is_directed_at_bot
from query import fetch_answer
from synonyms import synonym_for

# Clarence introduces himself
prompt.intro()

# The three questions to clarence
for i in range(3):
	question = prompt.ask_question(3-i).lower().split(" ")
	type = []
	subject = []
	if is_directed_at_bot(question):
		for j in question:
			if j in ["a", "the"]:
				# Skip a or the
				continue
			elif j in keywords.keywords:
				print(f"Found keyword {j}")
	else:
		# need to find subject
		for i in question:
			if i in keywords.keywords:
				syn, success = synonym_for(i)
				if success:
					print(fetch_answer(question, syn))
				else:
					print("i dunno. go look it up")	
				break
				
					

# Clarence excuses himself
prompt.outro()