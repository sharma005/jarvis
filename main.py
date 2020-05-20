import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your personal assistant. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # speak("Beep")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Sorry about that, I didn't hear anything. Please try again...")
        speak("Sorry about that, I didn't hear anything. Please try again...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    i = 1
    while i==1:
        i+=1
    # if True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to Wikipedia")
            
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://youtube.com")

        elif 'open google' in query:
            # webbrowser.open("google.com")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http:/stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\MP 3 SONGS\\Bollywood'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open videos' in query:
            vid_dir = 'D:\\PERSONAL PHOTOS VIDEOS\\Videos\\SONGS\\English Songs'
            videos = os.listdir(vid_dir)
            print(videos)
            os.startfile(os.path.join(vid_dir, videos[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Current time is -> "+ strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\abhis\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

        elif 'open sublime' in query:
            codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)

        # elif 'open brackets editor' in query:
        #     codePath = "C:\\Program Files (x86)\\Brackets\\Brackets.exe"
        #     os.startfile(codePath)

        elif 'open codeblocks' in query:
            codePath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codePath)

        elif 'open pubg' in query:
            codePath = "D:\\program files\\txgameassistant\\appmarket_8154875\\AppMarket.exe"
            os.startfile(codePath)

        elif 'email to abhishek' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aprofile005@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am unable to send this email")

print("""
*****************************************************************************
*      DONE !!...TO GIVE ANOTHER COMMAND, RUN THE PROGRAM AGAIN             *
*****************************************************************************
""")
# speak(" DONE !!...TO GIVE ANOTHER COMMAND, RUN THE PROGRAM AGAIN ")
