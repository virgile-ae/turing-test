#responds to user input with own questions
import random


def question_ask():
  """Returns a randomly generated question"""
  whatQ = ["name","favourite colour","favourite film","favourite TV show"]
  likeQ = ["Star Wars","heavy metal","the big bang theory"]
  howQ = ["old are you?","are you doing today","is the weather where you live"]
  randNum = 0
  randNum = random.randint(1,3)
  if randNum == 1:
    return (input("What is your" + whatQ[random.randint(0,len(whatQ))] + "?"))
  elif randNum == 2:
    return (input("Do You like" + likeQ[random.randint(0,len(likeQ))] + "?"))
  elif randNum == 3:
    return (input("Do You like" + howQ[random.randint(0,len(howQ))] + "?"))


    




