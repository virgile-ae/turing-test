# Contains functions to extract keywords which relate to:
# 		Who the question is for - your/you
#		What the question is about - jobs/interests/height
#		What type of question it is - who/what/when/do you/is
# Needs to be able to handle stuff like
#		Do you like - random yes or no
#		What do you think of - random i do(n't) like (thing) very much
# 		How is - random it is(n't) bad

# Words which indicate the type of question
qtype_words = open("./word_lists/qtypes.txt").read().splitlines()

# Words which indicate that the question is for the bot (as opposed to general facts)
qs_for_bot = [
	"you",
	"your",
	"clarence",
]

# Checks if the question is directed towards the bot or not
# If it is
#		The bot should either look up an answer or randomly generate one
# If it isn't
# 		The bot should look it up on google
def is_directed_at_bot(question):
	for i in question:
		if i in qs_for_bot:
			return True
	return False