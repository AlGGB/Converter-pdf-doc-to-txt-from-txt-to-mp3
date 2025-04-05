import os
from gtts import gTTS

text = "hello world"

output = gTTS(text, lang= 'es', slow=False)
output.save("helloworld.mp3")

os.system('start helloworld.mp3')

