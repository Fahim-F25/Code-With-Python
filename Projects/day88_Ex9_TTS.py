# import pyttsx3

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Set voice rate (speed)
# engine.setProperty("rate", 150)

# # Set volume (0.0 to 1.0)
# engine.setProperty("volume", 1.0)

# # Text you want to convert to speech
# text = "Hello! I am your Python text to speech assistant."

# names = ['Fahim', 'Fuhad', 'Siam', 'Shakib', 'Tamim', 'Badhon']

# # Speak the text
# # engine.say(text)
# for name in names:
#     engine.say(name)

# # Wait until speaking is finished
# engine.runAndWait()


#This is working guys!!
import win32com.client as wincl

speaker = wincl.Dispatch("SAPI.SpVoice")
names = ['Fahim','Fuhad','Siam','Shakib','Tamim','Badho']
for name in names :
    speaker.Speak(f"Shout out to {name}")
