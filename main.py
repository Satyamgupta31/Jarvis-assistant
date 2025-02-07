import openai  # pip install openai
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# OpenAI API key
# openai.api_key = 'your_openai_api_key'  # Replace with your OpenAI API key

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    # Takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')  # Replace with your email and password
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def ask_openai(query):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query,
            max_tokens=200,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        print(f"OpenAI Response: {answer}")
        speak(answer)
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't process that question right now.")

def execute_task(query):
    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to satyam' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "satyamkumarg089@gmail.com"  # Updated email address
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry my friend Satyam. I am not able to send this email.")

    else:
        speak("Let me think...")
        ask_openai(query)

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        execute_task(query)
