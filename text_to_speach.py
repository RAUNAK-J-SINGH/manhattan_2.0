import subprocess
import pyttsx3 as pyt


def text_to_speech(text):
   # Initialize the text-to-speech engine
   engine = pyt.init()

   # Set the voice
   engine.setProperty("voice", "english_male")

   # Set the speech rate
   engine.setProperty("rate", 150)

   # Convert the text to speech
   text = "This is a test of the text-to-speech engine."
   engine.say(text)

   # Play the speech
   engine.runAndWait()

    