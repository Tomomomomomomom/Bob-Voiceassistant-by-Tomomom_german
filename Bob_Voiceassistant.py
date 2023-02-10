import sys
sys.path.append("c:\\users\\8toma\\appdata\\local\\programs\\python\\python39\\lib\\site-packages")
sys.path.append("C:\\Users\\8toma\\source\\repos\\Bob Voiceassistant\\Bob Voiceassistant\\Skills\\tell_joke\\tell_joke.py")

import pyaudio
import speech_recognition as sr
import pyttsx3
import tell_joke

# Set the wake word
wake_word = "hey Bob"

# Define the functions for the available skills
def get_weather():
    # TODO: Write code to get the current weather and return a response
    return "The weather is currently sunny and warm."

def set_alarm(time):
    # TODO: Write code to set an alarm for the specified time and return a response
    return f"I have set an alarm for {time}."

def get_news():
    # TODO: Write code to get the latest news and return a response
    return "The latest news is that a new vaccine for COVID-19 has been developed."

def tell_joke():
    tell_joke.run_module()

# Initialize the dictionary of available skills
skills = {"weather": get_weather, "alarm": set_alarm, "news": get_news, "sag einen Witz": tell_joke}

# Set up the speech recognition
r = sr.Recognizer()

# Set up the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'german')

# Open a PyAudio stream for playing audio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, output=True)

# Continuously listen for the wake word
while True:
    with sr.Microphone() as source:
        print("Warte auf --> Hey Bob...")
        audio = r.listen(source)

    # Try to recognize the wake word
    try:
        wake_word_recognized = r.recognize_google(audio, language = "de-DE")
        if wake_word_recognized == wake_word:
            print("Wake word recognized")

            # Listen for the user's request
            with sr.Microphone() as source:
                print("Listening for request...")
                audio = r.listen(source)

            # Try to recognize the user's request
            try:
                request = r.recognize_google(audio, language = "de-DE")
                print(f"Request: {request}")

                # Check if the request is in the skills dictionary
                if request in skills:
                    # Call the corresponding function from the skills dictionary
                    response = skills[request]()
                else:
                    response = "gibts net."

                # Use the text-to-speech engine to generate audio for the response
                engine.say(response)
                engine.runAndWait()
                audio_data = engine.get_output()

                # Play the audio using the PyAudio stream
                stream.write(audio_data)
            except sr.UnknownValueError:
                engine.say("Kann ik nett.")
                engine.runAndWait()
                audio_data = engine.get_output()
                stream.write(audio_data)
            except sr.RequestError as e:
                print("Request error: {0}".format(e))
    except sr.UnknownValueError:
        pass
    except Exception as e:
        p.close()
stream.close()
