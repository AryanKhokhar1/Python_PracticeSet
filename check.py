# from PIL import Image
# img = Image.open("D:\\Twinkle.jpg")
# img.show()
import pyttsx3
n = '''Hey '''
engine = pyttsx3.init()
# setProperty function used for to set the property
engine.setProperty('rate',150) 
engine.setProperty('volume',100)
voices = engine.getProperty('voices')    
#engine.setProperty('voice', voices[0].id
engine.setProperty('voice', voices[1].id)
print(n)
engine.say(n)
engine.runAndWait()