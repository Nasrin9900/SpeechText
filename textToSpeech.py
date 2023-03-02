// google text to speech api import
from gtts import gTTS
//import os system for playing audio
import os
//Gujarati text which will be converted in audio
text1="મારું નામ નસરીન આસોફવાલા છે, હું એલજે યુનિવર્સિટીમાં આસિસ્ટન્ટ પ્રોફેસર છું"
//convert text to speech and specify the language
tts = gTTS(text1,lang='gu')
//save the audio
tts.save("one.mp3")
//play the audio
os.system("one.mp3")
