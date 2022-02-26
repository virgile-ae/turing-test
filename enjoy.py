# Contains functions to handle questions about enjoyment
from random import getrandbits 

# Returns a random bool which can be used to make decisions about whether or not clarence enjoys something
def rand_bool():
	return not getrandbits(1)

# Generates a response about question asking about an opinion on something
def opinion_on(kw):
	if rand_bool():
		return f"to be perfectly honest, i don't really like {kw}"
	return f"i actually quite like {kw}"

# Random reply to a yes-no question
def yes_no():
	if rand_bool():
		return "yep"
	return "nah"