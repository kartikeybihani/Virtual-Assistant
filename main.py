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
from twilio.rest import Client

from Alarm_Clock import Alarm
from News_Source import News
from Email_Source import Email

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Intro():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hi, Good Morning, I am zira, How can I help you")

    elif hour >= 12 and hour < 18:
        speak("Hi, Good Afternoon, I am Siri, How can I help you")

    else:
        speak("Hi, Good Evening, I am Siri, How can I help you")


def siri_command_process():

    listener = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")
            listener.pause_threshold = 0.6
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')

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
                    f"{rec_number}", f"{siri_command_process().capitalize()}", int(a), (int(mins) + 1.5))
                print("\nMessage has been sent successfully !")
                speak("Message has been sent successfully !")

            else:
                b = datetime.datetime.now().strftime("%H")  # 21
                pywhatkit.sendwhatmsg(
                    f"{rec_number}", f"{siri_command_process().capitalize()}", int(b), (int(mins) + 1.5))
                print("\nMessage has been sent successfully !")
                speak("Message has been sent successfully !")

        except Exception as e:
            print(e)
            speak("Sorry, can't send the message beacuse of some issue")

    elif "news" in command:
        try:
            News()
        except Exception as e:
            print("Sorry, I am not able to do that at the moment..")
            speak("Sorry, I am not able to do that at the moment..")

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
        speak("Let me check that for you")
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

    elif "call" in command or "phone" in command:
        account_sid = "YOUR ID"
        auth_token = "YOUR TOKEN"
        client = Client(account_sid, auth_token)

        try:
            # print("\nWhat should I say in the message ?")
            # speak("What should I say in the message ?")

            message = client.calls \
                .create(
                    to='YOUR PHONE NUMBER',
                    from_='YOUR ISSUED PHONE NUMBER',
                    twiml='<Response><Say>This is AI</Say></Response>'
                )

            print("Call has been made successfully !")
            speak("Call has been made successfully !")
            quit()

        except Exception as e:
            print(e)
            speak("Sorry, can't send the message beacuse of some issue")

    elif "joke" in command:
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
        print("Hi, I am siri ! Your Virtual Assistant . I was built at Kartikey's house")
        speak("Hi, I am siri ! Your Virtual Assistant . I was built at Kartikey's house")

    elif "where were you made" in command:
        print("Hi, I am siri ! Your AI Assistant . I was built at Kartikey's house")
        speak("Hi, I am siri ! Your AI Assistant . I was built at Kartikey's house")

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing" + song)
        print("Playing" + song)
        pywhatkit.playonyt(song)

    elif "bluetooth" in command:
        print("Looking for nearby bluetooth devices...")
        speak("Looking for nearby bluetooth devices")
        nearby_devices = bluetooth.discover_devices(lookup_names=True)

        for addr, name in nearby_devices:
            print("Address: ", addr)
            print("Name: ", name)

    elif "what" in command or "how" in command:
        client = wolframalpha.Client("YOUR API KEY HERE")
        res = client.query(command)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except Exception as e:
            print(e)
            speak("Sorry, I can't find any results but here's what I got for you")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            result = webbrowser.get(chrome_path).open(
                "https://www.google.com/search?q={}".format(command))

    elif "where" in command or "who is the" in command:
        client = wolframalpha.Client("YOUR API KEY HERE")
        res = client.query(command)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except Exception as e:
            speak("Sorry, I can't find any results, but here's what I got for you")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            result = webbrowser.get(chrome_path).open(
                "https://www.google.com/search?q={}".format(command))

    elif "wikipedia" in command or "who" in command or "tell me something about" in command or "search" in command or "what is" in command:
        command = command.lower()
        command = command.replace(
            "who" or "tell me something about" or "wikipedia" or "search", "")

        try:
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=3)
            print(results)
            speak("According to wikipedia " + results)
            print(wikipedia.page(f"\n{command}").url)
            speak("You can get more information from link given")

        except Exception as e:
            # print(e)
            speak("Sorry, I can't find any results, but here's what I got for you")
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
            msg = f"Hey\n \n{siri_command_process().capitalize()} \n\nRegards\nKartikey Bihani"

            Email(to, msg)
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

    elif 'thank you' in command or "ok  thank you" in command or "thank you  and bye" in command or 'thanx' in command or 'thanks' in command or 'good' in command or "nice" in command:
        speak("No problem . It's my pleasure to help you !")

    elif "you are bad" in command or "bad" in command:
        speak("That's not nice")
        quit()

    else:
        client = wolframalpha.Client("YOUR API KEY HERE")
        res = client.query(command)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except Exception as e:
            print(e)
            speak(
                "Sorry, I can't find any results for that, but here's what I got for you")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            result = webbrowser.get(chrome_path).open(
                "https://www.google.com/search?q={}".format(command))
            quit()


if __name__ == '__main__':
    Intro()
    while True:
        run_siri()
