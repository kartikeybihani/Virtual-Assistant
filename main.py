from Siri.Email_Source import Email
from Siri.News_Source import News
from Siri.Alarm_Clock import Alarm
import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import pyjokes
import smtplib
import os
import webbrowser
import wolframalpha
import bluetooth
import requests
from requests import get
import ctypes
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import psutil
from plyer import notification
import selenium
from selenium import webdriver
from time import sleep
import sys
import googletrans

gt = googletrans.Translator()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Intro():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hi, Good Morning, I am Siri, How can I help you")

    elif hour >= 12 and hour < 18:
        speak("Hi, Good Afternoon, I am Siri, How can I help you")

    else:
        speak("Hi, Good Evening, I am Siri, How can I help you")


greeting_words = {"hi": "hi", "hello": "hello",
                  "hey": "hey", "namaste": "namaste", "bonjour": "bonjour"}


def assistant_command_process():

    listener = sr.Recognizer()

    with sr.Microphone() as source_human_voice:
        print("\nListening...")
        listener.pause_threshold = 0.6
        voice = listener.listen(source_human_voice)

    try:
        command = listener.recognize_google(voice, language='hi-in')
        print("User said: " + command)

    except Exception as e:
        print(e)
        # print("I can't understand you . Please say that again")
        # speak("I can't understand you . Please say that again")
        return "none"

    command = command.lower()
    return command


def run_assistant():

    command_a = assistant_command_process()
    command = gt.translate(command_a).text

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    if "whatsapp message" in command:
        try:

            hours = datetime.datetime.now().hour  # 21
            mins = datetime.datetime.now().strftime("%M")

            speak("Please type the number you want to send the message to")
            number_input = input(
                "Please type the number you want to send the message to here: ")
            rec_number = f"+91{number_input}"

            print("\nWhat should I say in the message ?")
            speak("What should I say in the message ?")

            if hours > 0 and hours <= 12:
                a = datetime.datetime.now().strftime("%I")  # 09
                pywhatkit.sendwhatmsg(
                    f"{rec_number}", f"{assistant_command_process().capitalize()}", int(a), (int(mins) + 1.5))
                print("\nMessage has been sent successfully !")
                speak("Message has been sent successfully !")
                time.sleep(5)

            else:
                b = datetime.datetime.now().strftime("%H")  # 21
                pywhatkit.sendwhatmsg(
                    f"{rec_number}", f"{assistant_command_process().capitalize()}", int(b), (int(mins) + 1.5))
                print("\nMessage has been sent successfully !")
                speak("Message has been sent successfully !")
                time.sleep(5)

        except Exception as e:
            print(e)
            speak("Sorry, can't send the message beacuse of some issue")

    elif "battery" in command:
        def convertTime(seconds):
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            return "%d:%02d:%02d" % (hours, minutes, seconds)

        battery = psutil.sensors_battery()

        notification.notify(
            title="Battery Percentage",
            message=str(battery.percent)+"% Battery remaining",
            timeout=10
        )

        speak(f"Your Battery percentage is {battery.percent} %")
        print("Power plugged in: ", battery.power_plugged)

        time.sleep(5)

    elif "open gmail" in command:
        speak("Here you go!")
        webbrowser.get(chrome_path).open(
            "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

    elif "news" in command:
        try:
            News()
            speak("This news will be given to you by The Times of India")
        except Exception as e:
            print("Sorry, I am not able to do that at the moment..")
            speak("Sorry, I am not able to do that at the moment..")

    elif "mirror" in command:
        try:
            code_path = "C:\\Users\\Kartikey Bihani\\Documents\\scrcpy-win64-v1.17\\scrcpy.exe"
            os.startfile(code_path)
            speak("Here you go")
        except:
            speak("Sorry I am not able to do that. Maybe you should check your internet connection and please start usb debugging on your phone")

    elif "what are you doing" in command:
        speak("I am talking to you")

    elif "i am fine" in command or "i am good" in command:
        speak("Good to hear that")

    elif "reminder" in command or "alarm" in command or "remind" in command:
        try:
            Alarm(command)
        except Exception as e:
            print("Sorry, can't understand that. You should say the time in the sentence to set a reminder or alarm")
            speak("Sorry, can't understand that. You should say the time in the sentence to set a reminder or alarm")

    elif 'lock window' in command:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif "where i am" in command or "what's my location" in command or "tell me my location" in command or "where am i" in command:
        try:
            ipAdd = requests.get('https://api.ipify.org').text
            print(f"Your IP Address - {ipAdd}")
            url = f'https://get.geojs.io/v1/ip/geo/2409:4052:e05:bf2f:bcaf:3d8e:c389:a8a7.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            city = geo_data['city']
            country = geo_data['country']
            print(f"I think we are in {city}, {country}")
            speak(f"I think we are in {city}, {country}")
        except Exception as e:
            print(e)
            speak("Sorry, Due to some issue I am not able to find where we are")

    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif "how are you" in command or "how do you do" in command:
        answers = ("I am well !", "I am fine ! How can I help you ?", "Excellent !!", "I feel good !", "I am fine! Just exploring some new facts around the world",
                   "I am fine!, Just getting better day by day", "I am fine!, Just trying the things which I scare from")
        num = random.randrange(0, 7)
        print(answers[num])
        speak(answers[num])

    elif greeting_words.get(command.split(" ")[0]) == command.split(" ")[0] in command:
        print("Hi there ! How can I help you ? ")
        speak("Hi there ! How can I help you ? ")

    elif "who are you" in command:
        print("Hi, I am Your Virtual Assistant . I was built at Kartikey's house")
        speak("Hi, I am Your Virtual Assistant . I was built at Kartikey's house")

    elif "where were you made" in command:
        print("Hi, I am Your AI Assistant . I was built at Kartikey's house")
        speak("Hi, I am Your AI Assistant . I was built at Kartikey's house")

    elif "play" in command or "turn on" in command or "start" in command:
        song = command.replace("play", "")
        speak("Playing" + song)
        print("Playing" + song)
        pywhatkit.playonyt(song)

        return "none"

    elif "bluetooth" in command:
        print("Looking for nearby bluetooth devices...")
        speak("Looking for nearby bluetooth devices")
        nearby_devices = bluetooth.discover_devices(lookup_names=True)

        for addr, name in nearby_devices:
            print("Address: ", addr)
            print("Name: ", name)

    elif "what" in command or "how" in command:
        client = wolframalpha.Client("5GALLA-EAGHE3AREE")
        res = client.query(command)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except Exception as e:
            print(e)
            speak(
                "Sorry, I don't have any answer for that but here's what I got for you")
            result = webbrowser.get(chrome_path).open(
                "https://www.google.com/search?q={}".format(command))
            time.sleep(6)

    elif "where" in command or "who is the" in command:
        client = wolframalpha.Client("5GALLA-93E4G62GWW")
        res = client.query(command)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except Exception as e:
            speak(
                "Sorry, I don't have any answer for that, but here's what I got for you")
            result = webbrowser.get(chrome_path).open(
                "https://www.google.com/search?q={}".format(command))
            time.sleep(6)

    elif "wikipedia" in command or "who" in command or "tell me something about" in command or "search" in command or "what is" in command:
        command = command.lower()
        command = command.replace(
            "who" or "tell me something about" or "wikipedia" or "search", "")

        try:
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=3)
            # translator = Translator()
            # result = translator.translate(results, dest='hi')
            print(results)
            speak("Here you go, According to wikipedia " + results)
            print(wikipedia.page(f"\n{command}").url)
            speak("You can get more information from the link here")

        except Exception as e:
            # print(e)
            speak(
                "Sorry, I don't have any answer for that, but here's what I got for you")
            command = command.replace(
                "tell me something about" or "search" or "wikipedia", "")
            # command = command.replace("tell me something about", "")
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
            msg = f"Hey\n \n{assistant_command_process().capitalize()} \n\nRegards\nKartikey Bihani"

            Email(to, msg)
            print("\nEmail has been sent successfully !")
            speak("Email has been sent successfully !")
        except Exception as e:
            print(e)
            speak("Sorry, can't send the email beacuse of some issue")

    elif "open " in command:
        try:
            command = command.replace("open", "")

            speak("Here you go !")
            webbrowser.get(chrome_path).open(f"{command}.com")
        except Exception as e:
            speak(
                "Sorry, I am not able to do that at the moment...., but here's what I got for you")
            webbrowser.get(chrome_path).open(
                "https://www.google.com/search?q={}".format(command))
            time.sleep(5)

    elif "ok bye" in command or "exit" in command or "shut up" in command or "stop" in command or "bye" in command:
        print("Thank you for using me")
        speak("Thank you for using me")

    elif 'thank you' in command or "ok  thank you" in command or "thank you  and bye" in command or 'thanx' in command or 'thanks' in command or 'good' in command or "nice" in command:
        speak("No problem . It's my pleasure to help you !")

    elif "you are bad" in command or "bad" in command:
        speak("That's not nice")

    elif "none" in command:
        return

    else:
        speak("Sorry, I don't have an answer to that, but here's what I got for you")
        webbrowser.get(chrome_path).open(
            "https://www.google.com/search?q={}".format(command))


if __name__ == '__main__':
    while True:
        permission = assistant_command_process()
        if "hey siri" in permission or "ok siri" in permission or "hey Siri" in permission or "ok Siri" in permission:
            speak("Hi, how may I help you ?")
            while True:
                run_assistant()
        elif "ok bye" in permission or "exit" in permission or "shut up" in permission or "stop" in permission or "bye" in permission:
            speak("It's my pleasure to serve you")
            # speak("Thank you for using me")
            # sys.exit()
