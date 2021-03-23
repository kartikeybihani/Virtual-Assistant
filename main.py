import pyttsx3
import pyttsx3.drivers.sapi5
import pyttsx3.drivers
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import pyjokes
import smtplib
import os
import webbrowser
import wolframalpha

from info import sendEmail

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Intro():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hi, Good Morning! . I am Siri, How can I help you")

    elif hour >= 12 and hour < 18:
        speak("Hi, Good Afternoon! . I am Siri, How can I help you")

    else:
        speak("Hi, Good Evening! . I am Siri, How can I help you")


def siri_command_process():

    listener = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")
            listener.pause_threshold = 0.6
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')

            if "hey siri" in command:
                command = command.replace("hey siri", "")

            if "hey Siri" in command:
                command = command.replace("hey Siri", "")

            if "siri" in command:
                command = command.replace("siri", "")

            if "Siri" in command:
                command = command.replace("Siri", "")

            print("User said: " + command)

    except Exception as e:
        # print(e)
        speak("I can't understand you . Please say that again")
        print("I can't understand you . Please say that again")
        exit()
    return command


greeting_words = {"hi": "hi", "hello": "hello",
                  "hey": "hey", "namaste": "namaste", "bonjour": "bonjour"}
intro_words1 = {"how do you do": "how do you do", "how are you": "how are you"}


def run_siri():
    command = siri_command_process().lower()

    if "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif greeting_words.get(command.split(" ")[0]) == command.split(" ")[0] in command:
        print("Hi there ! How can I help you ? ")
        speak("Hi there ! How can I help you ? ")

    elif intro_words1.get(command.split(" ")[0]) == command.split(" ")[0] in command:
        print("I am fine ! How can I help you ?")
        speak("I am fine ! How can I help you ?")

    elif "who are you" in command:
        print("Hi, I am siri ! Your AI Assistant . I was built at Kartikey's house")
        speak("Hi, I am siri ! Your AI Assistant . I was built at Kartikey's house")

    elif "where were you made" in command:
        print("Hi, I am siri ! Your AI Assistant . I was built at Kartikey's house")
        speak("Hi, I am siri ! Your AI Assistant . I was built at Kartikey's house")

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing" + song)
        print("Playing" + song)
        pywhatkit.playonyt(song)

    elif "what" in command or "how" in command:
        client = wolframalpha.Client("5GALLA-9X67KG9GEK")
        res = client.query(command)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except Exception as e:
            print(e)
            speak("Sorry, I can't find any results")

    elif "where" in command or "who is the" in command:
        client = wolframalpha.Client("5GALLA-9X67KG9GEK")
        res = client.query(command)

        try:
            if "(data not available)":
                speak("Sorry, I can't find any results, but here's what I got for you")
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                result = webbrowser.get(chrome_path).open(
                    "https://www.google.com/search?q={}".format(command))
            else:
                print(next(res.results).text)
                speak(next(res.results).text)
        except Exception as e:
            speak("Sorry, I can't find any results, but here's what I got for you")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            result = webbrowser.get(chrome_path).open(
                "https://www.google.com/search?q={}".format(command))

    elif "wikipedia" in command or "who" in command or "tell me something about" in command or "search" in command:
        command = command.lower()
        command = command.replace(
            "who" or "tell me something about" or "wikipedia" or "search", "")
        # command = command.replace("who" and "tell" and "wikipedia" and "search" and "tell me something about" and "tell me about" and "hey Siri" and "hey siri tell me something about" and "hi" and "siri", "")
        try:
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=4)
            print(results)
            speak("According to wikipedia " + results)
        except Exception as e:
            # print(e)
            speak("Sorry, I can't find any results, but here's what I got for you")
            command = command.replace(
                "tell me something about" or "search" or "wikipedia", "")
            # command = command.replace("tell me something about", "")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            result = webbrowser.get(chrome_path).open(
                "https://www.google.com/search?q={}".format(command))

    elif "email" in command or "mail" in command:
        try:
            speak("Please type the receiver's email address below")
            rec_email = input(
                "\nPlease type the receiver's email address here: ")
            to = f"{rec_email}"

            print("\nWhat should I say in the email ?")
            speak("What should I say in the email ?")
            msg = f"Hey\n \n{siri_command_process()} \n\nRegards\nKartikey Bihani"

            sendEmail(to, msg)
            print("\nEmail has been sent successfully !")
            speak("Email has been sent successfully !")
        except Exception as e:
            print(e)
            speak("Sorry, can't send the email beacuse of some issue")

    elif "open " in command:
        command = command.replace("open", "")
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        speak("Here you go !")
        webbrowser.get(chrome_path).open(f"{command}.com")

    elif "ok bye" in command or "exit" in command or "shut up" in command or "stop" in command or "bye" in command:
        print("Thank you for using me")
        speak("Thank you for using me")
        quit()

    elif 'thank you' in command or 'thanx' in command or 'thanks' in command or 'good' in command:
        speak("No problem . It's my pleasure to help you !")


# Intro()
while True:
    run_siri()


# elif "open code" in command:
# 	code_path = "C:\\Users\\Kartikey Bihani\\AppData\\Local\\Programs\\VS Code\\Code.exe"
# 	os.startfile(code_path)
# elif "time" in command:
# 		speak("It is " + datetime.datetime.now().strftime("%I %M %p") + '.')
