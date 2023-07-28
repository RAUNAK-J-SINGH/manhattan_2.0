import subprocess
import pyttsx3


def code_text_to_speech(message):
   # Initialize the text-to-speech engine
   engine = pyttsx3.init()

   # Set the voice
   engine.setProperty("voice", "english_male")

   # Set the speech rate
   engine.setProperty("rate", 150)

   # Convert the text to speech
   # text = "This is a test of the text-to-speech engine."
   text = message
   engine.say(text)

   # Play the speech
   engine.runAndWait()

    