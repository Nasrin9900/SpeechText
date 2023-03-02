from googletrans import Translator
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    try:
        temp=r.recognize_google(audio_text)
        print("Text: "+temp)
        translator = Translator()
        translation = translator.translate(temp, src='en',dest='gu')
        print(translation.text)
    except:
         print("Sorry, I did not get that")
