import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

import re
import operator
listener = sr.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
import requests
import requests

def get_weather(city):
    api_key = "46b572dad9664851bba955##########"  # 🔁 Replace with your actual API key
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if "current" in data:
            temp = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            wind = data["current"]["wind_kph"]
            print(f"{city}: {condition}, {temp}°C, Wind {wind} kph")
            talk(f"The weather in {city} is {condition}, with a temperature of {temp} degrees Celsius and wind speed of {wind} kilometers per hour.")
        else:
            talk("Sorry, I couldn't get the weather information.")
    except Exception as e:
        print("Error:", e)
        talk("Something went wrong while getting the weather.")






        





def talk(text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

import google.generativeai as genai

genai.configure(api_key="AIzaSyCnDejKTeUJJixBs3Vlt7nvIegqdnk0ffk")  # 🔁 Paste your key here

def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        answer = response.text
        print("Gemini:", answer)
        talk(answer)
    except Exception as e:
        print("Error:", e)
        talk("Sorry, something went wrong with Gemini.")




               
    
    

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)

    elif 'who' in command:
      
        person= command.replace('who','')
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)
   
    elif 'what' in command:
      
        ans= command.replace('what','')
        info1=wikipedia.summary(ans,1)
        print(info1)
        talk(info1)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        jokes=pyjokes.get_joke()
        print(jokes)
        talk(jokes)
    elif 'calculate' in command or 'plus' in command or 'minus' in command or 'times' in command or 'divided by' in command:
        talk(calculate_expression(command))

    elif 'weather' in command:
        city = command.replace('weather in', '').replace('weather', '').strip()
        if city:
            get_weather(city)
         
        else:
            talk("Please tell me the city name for the weather update.")
    

   
    else:
        talk("please say the command again")
            

while True:
    run_alexa()

       
