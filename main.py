# Turing Test
# List who is in the group or if you are working alone.
# Shaurya and Virgile
import prompt
import loop

# Clarence introduces himself
prompt.intro()

# The three questions to clarence
for i in range(3):
	loop.handle_q(i)
# Clarence excuses himself
prompt.outro()