import os
from gtts import gTTS

text = "Buenos dias hoy gano la U"

output = gTTS(text, lang= 'es', slow=False)
output.save("output.mp3")

os.system('start output.mp3')

