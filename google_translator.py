
from googletrans import Translator

# Set the word to translate and the target language
word = "hello"
target_language = "de"

# Create a Translator object
translator = Translator()

# Translate the word
translation = translator.translate(word, dest=target_language).text

# Print the translation
print(translation)
