import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say any thing: ")
    audio = r.listen(source)
try:
    print("You say: ",r.recognize_google(audio))
except:
    print("Not get: ")
