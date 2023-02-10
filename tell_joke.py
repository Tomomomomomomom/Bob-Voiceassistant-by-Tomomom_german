import random

def tell_joke():
  # List of jokes
  jokes = [
    u"Was ist der Unterschied zwischen einem Apfel und einem Zitronenapfel? Ein Zitronenapfel hat keine Wuermer!",
    u"Wie nennt man eine Fliege ohne Fluegel? Einen Fussgaenger.",
    u"Warum hat der Hund das Haus verlassen? Weil es keine Leckerlis mehr gab.",
    u"Warum haben Baeume keine Freunde? Weil sie immer nur an sich denken.",
    u"Warum haben Elefanten keine Freunde? Weil sie immer alles vergessen.",
  ]

  # Select a random joke from the list and return it
  joke = random.choice(jokes)
  return joke

