import openai
import pyttsx3

# Set your OpenAI API key
openai.api_key = "your-api-key"

# Set the topic and the length of the song
topic = "love"
length = 4

# Generate the lyrics using gPT-3
model_engine = "davinci"
prompt = (f"Write a {length} verse song about {topic}")

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

lyrics = completions.choices[0].text

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice and speed
engine.setProperty('voice', 'german')
engine.setProperty('rate', 150)

# Split the lyrics into lines and sing them
lines = lyrics.split("\n")
for line in lines:
    engine.say(line)
    engine.runAndWait()

