import speech_recognition as sr
import pyttsx3
import webbrowser
import serial
import time
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


ser = serial.Serial("COM5")  # the port where your Arduino Board is


def run_christmas():
    command = take_command()
    print(command)
    if "christmas" in command:
        print("Christmas mode activated")
        talk("Christmas mode activated")
        pywhatkit.playonyt("Jingle Bells – Kevin MacLeod (No Copyright Music)")
        time.sleep(1)
        webbrowser.open("fire.gif")  # name of the picture in the directory as your main.py file
        time.sleep(3)
        while True:
            ser.write(b'H')  # H means HIGH (bright)
            time.sleep(2)  # wait 2 seconds
            ser.write(b'L')  # L means LOW (dark)
            time.sleep(1)  # wait 1 second
            ser.write(b'H')
            time.sleep(2)
            ser.write(b'L')
            time.sleep(1)
        ser.close()
        exit()
    else:
        talk("Please say the command again")


while True:
    run_christmas()
