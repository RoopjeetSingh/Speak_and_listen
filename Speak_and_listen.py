import speech_recognition as sr
import random
from gtts import *
import os
from pygame import *


def speak(text: str):
    """
    Given a text, the computer says the text
    :param text: The parameter that the user wants the program to speak
    :return:
    """
    try:
        tts_ = gTTS(text=text, lang='en')
        ran = random.randint(0, 1000000)
        audio_file = 'audio-' + str(ran) + '.mp3'
        tts_.save(audio_file)

        # Starting the mixer
        mixer.init()

        # Loading the song
        mixer.music.load("C:///Users/roopa/PycharmProjects/pokemon game/" + audio_file)

        # Start playing the song
        mixer.music.play()
        clock = time.Clock()
        # infinite loop
        while mixer.music.get_busy():
            clock.tick(60)
        mixer.music.unload()
        os.remove(audio_file)

    except gTTSError:
        pass


def listen_to_user(ask: str = None):
    """

    :param ask: This is a question that would be printed before asking the user to speak.
    :return: The text spoken by the user
    """
    r = sr.Recognizer()
    r.energy_threshold = 800
    if ask is not None:
        print(ask)
    else:
        print("Listening...")
    with sr.Microphone(sample_rate=44100) as source:
        audio = r.listen(source, phrase_time_limit=6)
        music_data = ""
        try:
            music_data = r.recognize_google_cloud(audio)
            music_data = music_data.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that")
        except sr.RequestError:
            print('\033[1m' + '\033[91m' +
                  'No internet' + '\033[0m' +
                  '''
Try:
Checking the network cables, modem, and router
Reconnecting to Wi-Fi
Running Windows Network Diagnostics
ERR_INTERNET_DISCONNECTED''')
        return music_data


def listen(ask=None):
    """
    This function can be used to record an answer to a question. The user could ask to "write"
    which would stop the program from listening to the user and instead ask for a written answer
    :param ask: This is a question that would be printed before asking the user to speak.
    :return: The text spoken by the user
    """
    while True:
        voice_data = listen_to_user(ask)
        if 'write' in voice_data:
            voice_data = input('-> ')
            if voice_data == 'speak':
                pass
            else:
                break
        elif 'right' in voice_data:
            voice_data_new = listen_to_user('Did you mean write? (yes/no)')
            if 'y' in voice_data_new:
                voice_data = input('-> ')
                if voice_data == 'speak':
                    pass
                else:
                    break
            else:
                pass
        else:
            break
    return voice_data
