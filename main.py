# Turing Test
# List who is in the group or if you are working alone.
# Shaurya and Virgile
from prompt import intro, outro
from handlers import handle_q

name = intro()

# Interrogation of clarence
for i in range(5):
    handle_q(name)

outro()
