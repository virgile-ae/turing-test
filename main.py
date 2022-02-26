# Turing Test
# List who is in the group or if you are working alone.
# Shaurya and Virgile
from enjoy import yes_no
import prompt
import keywords
from questions import QType, is_directed_at_bot, type_of_q
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
		type = type_of_q(question)
		if type == QType.Fact:
			pass
		elif type == QType.Opinion:
			pass
		elif type == QType.Unknown:
			pass
		elif type == QType.Yes_No:
			print(yes_no())
			continue
	else:
		# need to find subject
		print("debugging: google search")
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