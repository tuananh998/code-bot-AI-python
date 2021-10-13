import os 
import sys
import speech_recognition as sr 
import pyttsx3 
import time 
import datetime  


def speak(robot_brain): 
    print ("Trợ lí ảo : ",robot_brain ) 
    engine = pyttsx3.init ()
    voices = engine.getProperty ('voices')
    rate = engine.getProperty ('rate')
    volume = engine.getProperty ('volume')
    engine.setProperty ('volume', volume -0.0) 
    engine.setProperty ('rate', rate - 50) 
    engine.setProperty ('voice', voices [1].id) 
    engine.say(robot_brain)
    engine.runAndWait()


def get_audio_from_microphone():
    robot_ear = sr.Recognizer() 
    '''recording the sound'''
    with sr.Microphone () as source:
        print('FRIDAY:...')
        robot_ear.adjust_for_ambient_noise(source, duration=1)
        print ('FRIDAY:listening...')
        recorded_audio = robot_ear.listen(source,phrase_time_limit=4)
        print('FRIDAY:listened...')
    '''Recorgnizing the audio '''
    try:
        you = robot_ear.recognize_google(recorded_audio, language='en-US')
        print('người dùng : {}'.format(you))
        return you 
    except:
        robot_brain = 'ERROR!'
        speak (robot_brain)
        return 0

    
def stop():
    robot_brain = 'see you late!'
    speak(robot_brain )


def get_you():
    for i in range(3):
        text = get_audio_from_microphone()
        if text :
            return text.lower()
        elif i < 2 :
            speak(" I can't hear you what you say. Please try again !")
    time.sleep(3)
    stop()
    return 0


def main_brain ():
    robot_brain = "Hello! what is your name?"
    speak (robot_brain)
    name = get_you()
    robot_brain = f"Hello {name}"
    speak(robot_brain)
    while True :
        task = get_you()
        if "hello friday" in task : 
            robot_brain = f"Hello sir!"
            speak (robot_brain)
        else:
            robot_brain = "I can't understand your command "
            speak(robot_brain)





if __name__ =="__main__":
    main_brain()
    