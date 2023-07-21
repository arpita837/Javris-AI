import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    speak(f"The current time is {time_str}")


def wikipedia_search(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia, {result}")
    except wikipedia.exceptions.PageError:
        speak("I'm sorry, I couldn't find any information on that topic.")
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple matches for that topic. Please be more specific.")


def main():
    speak("Hi, I am your virtual assistant. How can I help you today?")
    while True:
        try:

            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)


            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")


            if "time" in query.lower():
                get_time()
            elif "search" in query.lower() or "wikipedia" in query.lower():
                speak("What do you want me to search on Wikipedia?")
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = recognizer.listen(source)
                search_query = recognizer.recognize_google(audio)
                wikipedia_search(search_query)
            elif "exit" in query.lower() or "quit" in query.lower():
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I couldn't understand your request.")
        except sr.UnknownValueError:
            speak("I'm sorry, I couldn't understand your request. Please try again.")
        except sr.RequestError:
            speak("Sorry, my speech service is not available at the moment. Please try again later.")

if __name__ == "__main__":
    main()
