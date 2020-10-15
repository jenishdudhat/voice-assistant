import speech_recognition as sr
from gtts import gTTS
import playsound

def engine(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice2.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def check(): #defining function
        
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)  #listening audio
        order=r.recognize_google(audio,language="en-in") #recognizing the audio
    e2.insert(tk.END,order)  #insert in textarea
    global x
    x=order.split(' ')  
