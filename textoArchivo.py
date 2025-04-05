from gtts import gTTS
import os

with open ('somefile.txt', 'r') as file:
           text = file.read()

output = gTTS(text, lang= 'es', slow=False)
output.save("somefile.mp3")

os.system('start somefile.mp3') #para ejecutar el nombre del archivo


