import pyttsx3
from src.utils import log_error

def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        log_error(f"Text-to-Speech error: {e}")
