import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import time
import pyautogui
import instaloader
import requests
import operator
import psutil
import speedtest
import nmap
import pyautogui as press
import pywhatkit
import phonenumbers
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
from phonenumbers import geocoder, carrier

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

apikey = "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"

def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {e}")

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        print("Good morning sir")
        speak("Good Morning Sir")

    elif 12 <= hour < 18:
        print("Good Afternoon sir")
        speak("Good Afternoon Sir")

    elif 18 <= hour <= 24:
        print("Good Evening sir")
        speak("Good Evening Sir")

    else:
        print("good night sir")
        speak("good night sir")

    speak("I Am jarvis Your Personal Voice Assistant. What Can I Do For You.....")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()

    except Exception as e:
        print(e)
        print("Say that again please....")
        #speak("Say that again please....")
        return "None"
    return query

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=b01915aec0c2438bb88fccf6ad2182ff'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def TaskExecution():
    wishMe()
    while True:
        query = takeCommand().lower()

        if "how are you" in query:
            speak("I'm fine sir, what about you...")

        elif 'hey' in query or 'hello' in query:
            speak("hello sir, may i help you with something..")

        elif 'also good' in query or 'fine' in query:
            speak("that's great to hear from you")

        elif 'thank you' in query or 'thanks' in query:
            speak("it's my pleasure sir.")

        elif "who are you" in query:
            speak("I am jarvis sir, your personal voice assistant ")

        elif "open command" in query:
            os.system("start cmd")
            speak("opening command prompt. please wait....")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...please wait')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia....")
            print(results)
            speak(results)

        elif "temperature" in query:
            search = "temperature in sindhanur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp_element = data.find("div", class_="BNeawe")
            if temp_element:
                temp = temp_element.text
                speak(f"current {search} is {temp}")
            else:
                speak("Sorry, I couldn't fetch the temperature at the moment.")

        elif "weather" in query:
            search = "weather in sindhanur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            weather_element = data.find("div", class_="BNeawe")
            if weather_element:
                temp = weather_element.text
                speak(f"current {search} is {temp}")
            else:
                speak("Sorry, I couldn't fetch the weather at the moment.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube Please Wait....")

        elif 'search on google' in query:
            speak("what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak("opening google. please wait....")

        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')
            speak("Opening google, please wait....")

        elif "hidden menu" in query:
            press.hotkey('winleft', 'x')
            speak("showing hidden menu, please wait..")

        elif "task manager" in query:
            press.hotkey('ctrl', 'shift', 'esc')
            speak("opening task manager, please wait..")

        elif "task view" in query:
            press.hotkey('winleft', 'tab')
            speak("viewing task, please wait...")

        elif "close the app" in query:
            press.hotkey('alt', 'f4')
            speak("closing app...")

        elif "setting" in query:
            press.hotkey('winleft', 'i')
            speak("opening setting, please wait...")

        elif "new virtual desktop" in query:
            press.hotkey('winleft', 'ctrl', 'd')
            speak("making a new desktop, please wait")

        elif 'play' in query:
            song = query.replace('play', ' ')
            speak("playing" + song + "please wait...")
            pywhatkit.playonyt(song)

        elif 'open facebook' in query:
            webbrowser.open('https://www.facebook.com/')
            speak("Opening Facebook Please Wait....")

        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com/')
            speak("Opening Instagram Please Wait....")

        elif "open notepad" in query:
            speak("opening notepad, please wait.....")
            codePath = "C:\\Windows\\System32\\notepad.exe"
            notepad = subprocess.Popen(codePath)

        elif "close notepad" in query:
            speak("closing notepad, please wait....")
            codePath = "C:\\Windows\\System32\\notepad.exe"
            notepad = subprocess.Popen(codePath)
            notepad.terminate()

        elif 'open code' in query:
            codePath = "C:\\Users\\md39k\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)
            speak("Opening Visual Studio Code Please Wait....")

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "logout" in query:
            speak('logging out in 5 second')
            os.system("shutdown - l")

        elif 'shutdown the system' in query:
            speak("Ok Sir, Your System Is Going to Shutdown In 5 Second")
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            speak("restarting your system..., Please Wait.")
            os.system("shutdown /r /t 5")

        elif 'temperature' in query:
            search = "temperature in sindhanur"
            url = f"https://www.google.com/search?={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif 'switch the Window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'tell me news' in query:
            speak("Please Wait. Feteching the latest news..")
            news()

        elif 'how much power left' in query or 'how much power we have' in query or 'battery' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f'sir our system have {percentage} percent battery')
            if percentage >= 75:
                speak("we have enough power to continue our work")
            elif 40 <= percentage <= 75:
                speak("we should connect our system to charging point to charge our battery")
            elif 15 <= percentage <= 30:
                speak("we don't have enough power to work, please connect to charging")
            elif percentage <= 15:
                speak("we have very low power, please connect to charging the system will shutdown very soon")

        elif 'take a screenshot' in query:
            speak("sir, please tell me the name for screenshot file")
            name = takeCommand().lower()
            speak("please hold the screen for few seconds, i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done, the screenshot is saved in our main folder. now i am ready for next command")

        elif 'you can sleep' in query or 'sleep' in query or 'sleep now' in query:
            speak("Thanks you sir, i am going to sleep you can call me anytime..")
            break

def wakeup():
    print("welcome back sir")
    speak("welcome back sir")
    print("jarvis is now online")
    speak("jarvis is now online")
    print("please say wake up to activate jarvis")
    speak("please say wake up to activate jarvis")
    while True:
        query = takeCommand()
        if 'jarvis' in query:
            TaskExecution()

        elif 'goodbye jarvis' in query or 'go now' in query:
            speak("thank you for using jarvis sir, have a good day")
            exit()

if __name__ == "__main__":
    wakeup()