from secrets import choice
import speech_recognition as sr 
import pyttsx3
import webbrowser
import wikipedia
import datetime
import time
import os
import requests
import json
import pyjokes
import smtplib
import random

engine = pyttsx3.init('sapis 5')
voice = engine.getProperty('voice')
engine.setProperty('voice', voice[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def talkCommand():
    s = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        s.pause_threshold = 1.5
        audio = s.listen(source)

    try:
        print('Recognizing...')
        query = s.recognize_google(audio, language = 'en')
        print(f"You said:{query}\n")

    except Exception as e:
        print(e.message)
        print("Come again, I didn't get you clearly")
        talk("Come again, I didn't get you clearly")
        return "None"
    
    return query

def greetMe():
    hour = int(datetime.datetime.now().hour)
    time = datetime.datetime.now().strftime("%I:%M:%S")
    
    if 5 <= hour < 12:
        talk("Good Morning")

    elif 12 <= hour < 16:
        talk("Good Afternoon")

    else:
        talk("Good Evening")

    talk("I am Groot, and you are? ")
    name = (input('Name: '))
    talk(f"{name}, How may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('philosiama@gmail.com', 'Password')
    server.sendmail('philosiamas@gmail.com', to, content)
    server.close()

    

if __name__ == "__main__":
    greetMe()
    while True:
        query = talkCommand().lower()

        if 'who are you' or 'who made you' in query:
            i_do = [ 'send emails' ,'send whatsapp messages', 
                      'search on google and wikipedia',
                      'check time and date',
                      'tell you jokes','play music on spotify and youtube',
                      'give you daily trends and gossips',
                      'give you the latest released music, movies and tv series',
                      'among other amazing stuff']

            talk(f"I am Groot. I was created by Philbert Siama. I can {i_do}")

        elif ' time' in query:
            strftime = datetime.datetime.now().strftime("%I:%M:%S:%P")
            talk("The current time is" + strftime)
        
        elif 'date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            talk("the current Date is" + date + month + year)

        elif 'joke' or 'jokes' or 'crack my ribs' in query:
            joke = pyjokes.get_joke()
            talk(joke)

        elif 'google' or 'search' in query:
            query = query.replace('google','search','')
            search = webbrowser.open(query)
            talk('searching google...')
            talk(search)

        elif 'wikipedia' in query:
           query = query.replace('wikipedia','')
           search = wikipedia.wikipedia(search)
           talk('searching wikipedia...')
           talk(search)

        elif 'record' or 'take note' or 'note' in query:
            open = os.path.isdir(C:\Users\Siama\Desktop\notes\EMS\records)

        elif 'news' or 'headlines' in query:
            query = query.replace('news','headlines','')
            search = webbrowser.open(query)

        elif 'youtube' in query:
           query = query.replace('youtube','')
            search = webbrowser.open(query)
            talk(search)

        elif 'music' or 'song' or 'songs' in query:
            open = os.add_dll_directory.(path)
            talk('opening music...')
        
        elif 'send' or 'message' in query:
            query = talkCommand().lower
            talk('sending message on whatsapp')

        elif 'remind' in query:
            open = os.path.join(C:\Users\Siama\Desktop\notes\EMS\records)
        
        elif 'sports' in query:
            search = webbrowser.open(query)
            talk(search)

        elif 'twitter' in query:
            tweet = webbrowser.get(profile.twitter_url)
            talk('opening twitter feed...')

        elif 'facebook' in query:
            fb = webbrowser.get(profile.facebook_)
            talk('opening facebook...')

        elif 'instagram' in query:
            inst = webbrowser.get(profile.instagram)
            talk('Opening instagram...')

        elif 'email to' or 'send email' in query:
            try:
                talk("What should I say?")
                content = query
                to = "ReciversEmail@gmail.com"
                sendEmail(to, content)
                talk("Email has been sent!")
            except Exception as e:
                print(e)
                talk("Sorry, Email not sent, try again.")
        
        foods = ['ugali and omena', 'Ugali and Eggs', 'Fish and Ugali',
                 'ugali and meat', 'Ugali and Matumbo', 'ugali and chicken','ugali and Liver',
                 'rice and eggs','rice and fish','rice and meat','rice and matumbo',
                 'rice and chicken','rice and liver','yams/bananas and meat','yams,bananas and beans','yams/bananas and chicken'
                 ]

        elif 'eat' in query:
            eat_food = random.choice(foods)
            talk(f"Today, you'll have to eat, {eat_food}")
            
        elif 'weather' in query:
            temperature = 


        

        











