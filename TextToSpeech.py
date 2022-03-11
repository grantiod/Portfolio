from gtts import gTTS
import os

print("Enter your text below:")
text = input()
speech = gTTS(text = text, lang = 'en', slow = False)
speech.save("output.mp3")
os.system("start output.mp3")