import pywhatkit
import wikipedia
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import os

# Initialize the recognizer and the TTS engine 
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice command from the user
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not get that.")
            return "None"
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return "None"
#funcation for alarm 
def alarm(command):
    timehere = open("Alarmtext.txt","a")
    timehere.write(command)
    timehere.close()
    os.startfile("alarm.py")
#funcation for greet according to time
def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,dude")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,dude")

    else:
        speak("Good Evening,dude")

# Function to take text input from the user
def get_input():
    choice = input("Would you like to speak or type your command? (s/t): ").strip().lower()

    if choice == "s":
        return listen()
    elif choice == "t":
        return input("Please type your command: ").strip().lower()
    else:
        speak("Invalid input. Please say or type 's' or 't'.")
        return get_input()
# funcation for open goggle
def searchGoogle(command):
    if "google" in command:
        import wikipedia as googleScrap
        command = command.replace("jarvis","")
        command = command.replace("google search","")
        command = command.replace("google","")
        speak("This is what I found on google")
      

        try:
            pywhatkit.search(command)
            result = googleScrap.summary(command,1)
            speak(result)

        except:
            speak("No speakable output available")
#funcation for you tube
def searchYoutube(command):
    if "youtube" in command:
        speak("This is what I found for your search!") 
        command = command.replace("youtube search","")
        command = command.replace("youtube","")
        command = command.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + command
        webbrowser.open(web)
        pywhatkit.playonyt(command)
        speak("Done, Sir")
# funcation for weather
def searchweather(command):
    if "weather" in command:
        speak("This is what I found for your search!") 
        command = command.replace("weather search","")
        command = command.replace("weather","")
        command = command.replace("jarvis","")
        web  = "https://www.accuweather.comt/results?search_query=" + command
        webbrowser.open(web)
        pywhatkit.playonyt(command)
        speak("Done, Sir")


# def searchWikipedia(command):
#     if "wikipedia" in command:
#         speak("Searching from wikipedia....")
#         command = command.replace("wikipedia","")
#         command = command.replace("search wikipedia","")
#         command = command.replace("jarvis","")
#         results = wikipedia.summary(command,sentences = 2)
#         speak("According to wikipedia..")
#         print(results)
#         speak(results)

# Main function for the AI assistant
def ai_assistant():
    greetMe()
    speak("how can I assist you?")
    while True:
        command = get_input()

        if command == "None":
            continue

        # Logic to handle different commands
        if "hello" in command:
            speak("Hello! How can I help you?")
        
        elif "how are you" in command:
            speak("I'm just a program, but I'm doing great! How about you?")
        #for time 
        elif "time" in command:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            speak(f"The time is {current_time}")
        #general communication
        elif "fine" in command:
            speak("That's great, sir.")
        elif "how are you" in command:
            speak("Perfect, sir.")
        elif "thank you" in command:
            speak("You are welcome, sir.")
        elif "about designer" in command:
            speak("Juhi,Piyush,Akash...")
        

        # elif "temperature" in command:
        #     search = "temperature in gunupur"
        #     url = f"https://www.google.com/search?q={search}"
        #     r  = requests.get(url)
        #     data = BeautifulSoup(r.text,"html.parser")
        #     temp = data.find("div", class_ = "BNeawe").text
        #     speak(f"current{search} is {temp}")
            
        # elif "weather" in command:
        #     search = "temperature in gunupur"
        #     url = f"https://www.google.com/search?q={search}"
        #     r  = requests.get("https://weather.com/en-IN/weather/tenday/l/Gunupur+Odisha?canonicalCityId=efb0e14f62d5bc7798ba7c6510559ddc617d914f6a5a18f23d5d566b5e918653")
        #     data = BeautifulSoup(r.text,"html.parser")
        #     temp = data.find("div", class_ = "BNeawe").text
        #     speak(f"current{search} is {temp}")
#for alarm
        elif "set an alarm" in command:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")
#open apps 
        elif "open" in command:
            from Dictapp import openappweb
            openappweb(command)
        elif "close" in command:
            from Dictapp import closeappweb
            closeappweb(command)
#for remender
        elif "set reminder" in command:
            rememberMessage = command.replace("remember that","")
            rememberMessage = command.replace("jarvis","")
            speak("You told me to remember that"+rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in command:
            remember = open("Remember.txt","r")
            speak("You told me to remember that" + remember.read())
#for shutdown the sys
        elif "shutdown the system" in command:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")

            elif shutdown == "no":
                break

        elif "google" in command:
            searchGoogle(command)

        

        elif "play a game" in command:
                    from game import game_play
                    game_play()
        elif "open youtube" in command:
            searchYoutube(command)
        # elif "weather" in command:
        #     searchweather(command)
        # elif "wikipedia" in command:
        #     searchWikipedia(command)
        #final sleep
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        
        else:
            speak("Sorry, I didn't understand that.")

# Run the assistant
if _name== "main_":
    ai_assistant()
