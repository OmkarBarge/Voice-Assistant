import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time

#------------------------------------
# if pyaudio related any issue occurs try below commands
#1.'pip install pipwin'
#2.'pipwin install pyaudio'
#------------------------------------

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:            #to start microphone for recording
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)   #for noise cancellation of recorded audio
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            # print(data)
            return data
        except sr.UnknownValueError:
            print('Retry Unable to Understand.')

def text_to_speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)  #voices[1] for female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)           #for speaking speed control
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    if 'omkar' in sptext().lower():
        while True:
            data_1 = sptext().lower()
            if 'your name' in data_1:
                name = 'my name is jin'
                text_to_speech(name)

            elif 'old are you' in data_1:
                age = 'im 31 year old'
                text_to_speech(age)

            elif 'time' in data_1:
                time = datetime.datetime.now().strftime('%I%M%p')
                text_to_speech(time)

            elif 'youtube' in data_1:
                webbrowser.open('https://www.youtube.com/')

            elif 'google' in data_1:
                webbrowser.open('www.google.co.in')

            elif 'joke' in data_1:
                joke_1 = pyjokes.get_joke(language='en',category='all')
                print(joke_1)
                text_to_speech(joke_1)

            elif 'search' in data_1:
                data_slice = data_1[6:]
                webbrowser.open(data_slice)

            elif 'exit' in data_1:
                text_to_speech('thank you')
                break

            # time.sleep(5)               #5 sec time delay for repeat the program again


    else:
        # print('You are talking to me?')
        text_to_speech('are you talking to me then activate me with omkar')