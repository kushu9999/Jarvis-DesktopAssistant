import pyttsx3 # text to speech library
import datetime # importing date and time
import speech_recognition as sr # impoting speechRecognition library
import wikipedia # installing wikipedia library
import webbrowser # importing web browser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5') # it's microsoft api for voice
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id) # 2 types of voices 0 gril 1 boy

def speak(audio): #  speaking function
    engine.say(audio)
    engine.runAndWait()

def wishMe(): # greeting function
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour <18 :
        speak("Good Afternoon")

    else :
        speak("Good Evening")
    speak("I am your assistant David , Please tell me how may i help you")

def takeCommand():
    '''
    it takes microphone from the user and return string output

    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)


    try: # we use try if error may come
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n") 
    
    except Exception as e :
        print(e)
        print("say that again please....")
        #speak("say that again please....")
        return "None"
    return query

def sendEmail(to,content):
        server = smtplib.SMTP('smtp.gmail.com' , 587)
        server.ehlo()
        server.starttls()
        server.login('your-id@gmail.com','your-password')
        server.sendmail('your-id@gmail.com', to ,content)
        server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    

       query = takeCommand().lower()

       # logic for executing tasks based on query

       if 'who' in query:
           print('Just wait....')
           speak('Just wait....')
           query = query.replace("who","")
           results = wikipedia.summary(query , sentences=2)
           print(results)
           speak(results)

       elif 'open youtube' in query :
            webbrowser.open("youtube.com")

       elif 'open google' in query :
            webbrowser.open("google.com")

       elif 'open instagram' in query :
            webbrowser.open("instagram.com")

       elif 'open stackoverflow' in query :
            webbrowser.open("stackoverflow.com")

       elif 'open medium' in query :
            webbrowser.open("medium.com")

       elif 'internet speed'  in query :
            webbrowser.open("fast.com")

       elif 'open udemy' in query :
            webbrowser.open("udemy.com")

       elif 'play song'  in query :
           songs_dir = 'H:\\Videos'
           songs = os.listdir(songs_dir)
           os.startfile(os.path.join(songs_dir,random.choice(songs))) #random.choice(songs)

       elif 'the time' in query :
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir, the time is {strTime}")
           print(f"sir, the time is {strTime}")

       elif 'chrome' in query :
           chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
           os.startfile(chrome)

       elif 'email' in query :

           try:
               speak("what should i say?")
               content  = takeCommand()
               to = "your-id@gmail.com"
               sendEmail(to , content)
               speak("Email has been sent !")
           except Exception as e:
                print(e)
                speak("Sorry, this time i unable to send the mail services")

       elif 'quit' in query:
           exit()

     


            
           
