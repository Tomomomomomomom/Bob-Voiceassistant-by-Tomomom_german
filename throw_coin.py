import random

def throw_coin():
  # Generate a random number between 0 and 1
  result = random.randint(0, 1)

  # Return "Kopf" if the result is 0, or "Zahl" if the result is 1
  if result == 0:
    return "Kopf"
  else:
    return "Zahl"

