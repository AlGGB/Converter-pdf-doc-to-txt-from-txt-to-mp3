from gtts import gTTS
import os

with open ('ella2.txt', 'r') as file:
           text = file.read()

output = gTTS(text, lang= 'es', slow=False)
output.save("ella2.mp3")

os.system('start ella2.mp3') #para ejecutar el nombre del archivo


