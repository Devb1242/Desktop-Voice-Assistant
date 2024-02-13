import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Dev!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon Dev!")

    elif hour>=16 and hour<20:
        speak('Good Evening Dev!')

    else:
        speak('Good Night Dev')

    speak("I am Jarvis. How may I assist you? ")

def takeCommand():   
    # It takes microphone input from the user and returns string input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        #print(e)
        print("Say the again...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    
    #Login for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening youtube... Please wait')
            webbrowser.open("youtube.com")

        elif 'open google' in query: 
            speak('Opening google... Please wait')
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak('Opening stackoverflow... Please wait')
            webbrowser.open("stackoverflow.com")
        
        elif 'open w3 school' in query:
            speak('Opening w3school... Please wait')
            webbrowser.open("w3schools.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak("Its")
            speak(strTime)

        elif 'name' in query:
            speak("Your name is Dev Patel")  

        elif 'open visual studio code' in query:
            codepath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open soptify' in query:
            codepath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath) 

        elif 'quit' in query:
            speak("See you soon... Byyy!")
            exit()
