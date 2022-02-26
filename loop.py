# Contains the function which is to be looped over in main
import keywords
import prompt
from enjoy import yes_no, opinion_on
from questions import QType, is_directed_at_bot, type_of_q
from query import fetch_answer
from synonyms import synonym_for

def clean_final(word):
	if not word[-1].isalpha():
		return word[:-1]

def handle_q(i):
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
			if "do" in question and ("like" in question or "enjoy" in question):
				print(opinion_on(clean_final(question[-1])))
			else:
				print(yes_no())
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