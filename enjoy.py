# Contains functions to handle questions about enjoyment
from random import getrandbits 

# Returns a random bool which can be used to make decisions about whether or not clarence enjoys something
def rand_bool():
	return not getrandbits(1)