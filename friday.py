from asyncio import exceptions
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5') #its a API and used for inbuilt voices in windows
voices = engine.getProperty('voices')#this are the two voices which are present in my computer =[<pyttsx3.voice.Voice object at 0x000001B43B05B010>, <pyttsx3.voice.Voice object at 0x000001B43B05B190>]
engine.setProperty('voice',voices[1].id)#its a male voice=[TTS_MS_EN-US_DAVID_11.0] 



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good AfterNoon!")
    else:
        speak("Good Evening ")
    speak("I am Friday . Please tell me how may I help you  ")


def takecommand():    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold=1.25
        audio =  r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except exceptions as e:
        #print(e)

        print("Say that again please......")
        return "None"
    return query
def manual():
    print('Hello!')
    print('I am Jarvis. Your voice assistant.')
    print('I can assist you with the following tasks:')
    print('1) Search for something on Wikipedia.')
    print('2) Access YouTube.')
    print('3) Access Google.')
    print('4) Access WhatsApp.')
    print('5) Access Netflix.')
    print('6) Access Spotify.')
    print('7) Tell you the time.')
    print('8) Open Visual Studio Code.')

if __name__ == "__main__":
    WishMe()
    manual()
    wish = True
    while wish == True:
        query = takecommand().lower()
        
        if 'wikipedia' in query:
            speak('Serching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif "who are you" in query:
                speak('Hello!')
                speak('I am Friday. Your voice assistant.')
                speak('I can assist you with the following tasks:')
                speak('I can Search for something on Wikipedia.')
                speak('I can Access YouTube.')
                speak('I can Access Google.')
                speak('I can Access WhatsApp.')
                speak('I can Access Netflix.')
                speak('I can Access Spotify.')
                speak('I can Tell you the time.')
                speak('I can Open Visual Studio Code.')
        
        elif 'open youtube' in query or 'access youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query or 'access google' in query:
            webbrowser.open('google.com')
        
        elif 'open amazon' in query or 'access amazon' in query:
            webbrowser.open('amazon.in')
        
        elif 'open whatsapp' in query or 'access whatsapp' in query:
            webbrowser.open('web.whatsapp.com')
        
        elif 'open facebook' in query or 'access facebook' in query:
            webbrowser.open('facebook.com')
        
        elif 'open spotify' in query or 'access spotify' in query:
            spo = "C:\\Users\\nithi\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spo)
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")
        
        elif 'open netflix' in query or 'access netflix' in query:
            webbrowser.open('netflix.com')
        
        elif 'open code' in query or 'access code' in query:
            codePath = "C:\\Users\\nithi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open moodle' in query or 'access moodle' in query:
            webbrowser.open('learn.gitam.edu')
        
        elif 'open student portal' in query or 'access student portal' in query:
            webbrowser.open('login.gitam.edu')
        
        elif 'goodbye' in query:
            speak('Goodbye')
            wish = False

