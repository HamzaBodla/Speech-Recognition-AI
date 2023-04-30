import pyglet as pg
import speech_recognition as sr
import pyttsx3
from commander import Commander

def init():
    pg.resource.path = ['audio']
    pg.resource.reindex()
    file = pg.resource.media('out-of-nowhere-message-tone.mp3')
    window = pg.window.Window(visible=False)
    cmd = Commander()
    return file, window, cmd

def close_application(window):
    window.close()

def speech_recognition(file, cmd):
    r = sr.Recognizer()
    running = True

    while running:
        print("listening...")
        file.play()

        with sr.Microphone() as source:
            print("say something")
            audio = r.listen(source)

        file.play()

        try:
            command = r.recognize_google(audio)
        except:
            print("Couldn't understand")
            continue

        if command.lower() in ['stop', 'quit', 'cancel', 'exit']:
            print("You said the following:")
            print(command)
            running = False
        else:
            print("You said the following:")
            print(command)
            cmd.discover(command)

def main():
    file, window, cmd = init()

    speech_recognition(file, cmd)

    close_application(window)

if __name__ == "__main__":
    main()