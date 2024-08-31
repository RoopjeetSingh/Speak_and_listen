import speech_recognition as sr
import random
from gtts import *
import os
from pygame import *


def speak(text: str, big_text_test = False):
    try:
        tts_ = gTTS(text=text, lang='en')
        ran = random.randint(0, 1000000)
        audio_file = 'audio-' + str(ran) + '.mp3'
        tts_.save(audio_file)
        # vlc_instance = vlc.Instance()
        # player = vlc_instance.media_player_new()
        # media = vlc_instance.media_new("C:///Users/roopa/PycharmProjects/pokemon game/" + audio_file)
        # player.set_media(media)
        # player.play()
        # time.sleep(1.5)
        # duration = player.get_length() / 1000
        # time.sleep(duration)

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
            # if big_text_test:
            #     query = input("e for end (only for testing) ")
            #     if query == 'e':
            #         # Stop the mixer
            #         mixer.music.stop()
            #         break
        mixer.music.unload()
        os.remove(audio_file)

    except gTTSError:
        pass


def record_audio(ask: str = None):
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
            music_data = r.recognize_google(audio)
            music_data = music_data.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that")
        except sr.RequestError:
            print('\033[1m' + '\033[91m' +
                  'No internet' + '\033[0m' +
                  '''
Try:
Checking the network cables, modem, and router
Reconnecting to Wi-Fi
Running Windows Network Diagnostics
ERR_INTERNET_DISCONNECTED''')
            speak('You are not connected to a WiFi', False)
        return music_data


def record_real(ask=None):
    while True:
        voice_data = record_audio(ask)
        if 'write' in voice_data:
            voice_data = input('-> ')
            if voice_data == 'speak':
                pass
            else:
                break
        elif 'right' in voice_data:
            voice_data_new = record_audio('Did you mean write? (yes/no)')
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
speak('hi, i am speaker')