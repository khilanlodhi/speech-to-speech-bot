import speech_recognition as sr
from src.utils import log_error

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source)  
            recognizer.energy_threshold = 2000  
            print("Listening...")
            
            
            audio = recognizer.listen(source, timeout=30, phrase_time_limit=10)  
            print("Processing...")
            print(f"Audio captured: {audio}")  

            
            with open("captured_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())

            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Speech Recognition could not understand the audio.")
            log_error("Speech Recognition could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Speech Recognition error: {e}")
            log_error(f"Speech Recognition error: {e}")
            return None
        except sr.WaitTimeoutError:
            print("Speech Recognition timed out while waiting for input.")
            return None
        except Exception as e:
            print(f"Error during speech recognition: {e}")
            log_error(f"Error during speech recognition: {e}")
            return None
