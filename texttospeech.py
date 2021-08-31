import pyttsx3
text_speech = pyttsx3.init()
answer = input("what u want to convert")
text_speech.say(answer)
text_speech.runAndWait()