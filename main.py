# Turing Test
# List who is in the group or if you are working alone.
# Shaurya and Virgile
import prompt
import loop

# Clarence introduces himself
name = prompt.intro()

# The three questions to clarence
for i in range(5):
    loop.handle_q(name)
# Clarence excuses himself
prompt.outro()
