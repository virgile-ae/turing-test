# Contains functions which are used to find synonyms for the subject of the question
from keywords import synonyms

# Takes a word and checks if it is a keyword
# Returns the word that it is a synonym for and a bool indicating success
def synonym_for(kw):
	for k, v in synonyms.items():
		if kw in v:
			return k, True
	return "", False

# Finds if a word is a keyword or not
# Returns 
def is_keyword(word):
	pass	