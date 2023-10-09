from googlecontroller import GoogleAssistant
import config

home = GoogleAssistant(host = config.google_home)

def tts_say(message):
    home.say(message)

if __name__ == '__main__':
    tts_say('hello')
