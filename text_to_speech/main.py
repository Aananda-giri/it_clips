import pyttsx3
# from PyQt5.QtCore import QObject, pyqtSignal

class TTS:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()   # close the engine
