import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("User said:", query)
            return query.lower()
        except Exception as e:
            print("Sorry, I could not understand. Can you please repeat?")
            return ""


def greet():
    current_hour = datetime.datetime.now().hour
    if 0 <= current_hour < 12:
        speak("Good morning!")
    elif 12 <= current_hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def handle_commands(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak("The current time is " + current_time)
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak("Today's date is " + current_date)
    elif "search" in command:
        speak("What would you like me to search for?")
        search_query = recognize_speech()
        if search_query:
            url = "https://www.google.com/search?q=" + search_query
            webbrowser.open(url)
            speak("Here are the search results for " + search_query)
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

# Main function
def main():
    greet()
    while True:
        command = recognize_speech()
        handle_commands(command)

if __name__ == "__main__":
    main()

