import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour <= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir. Please tell me how may I help You?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognize...")
        query = r.recgnize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
       # print(e)
        print("Say that again please ...")
        return "None"
    return query

    if __name__ == "__main__":
        wishme()
    query = takecommand().lower()

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
        music_dir = 'D:\\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:S")
        speak(f"Sir, the time is {strtime}")

    elif 'open code' in query:
        codepath = "F:\\py\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    elif 'email to harry' in query:
        try:
            speak("What should I say?")
            content = takecommand()
            to = "yourEmail@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
