import tkinter as tk
from tkinter import ttk
import pyttsx3
import webbrowser
import datetime
import random
import subprocess
import time
import speech_recognition as sr
import threading

# Define the login credentials (For simplicity, this can be hardcoded)
USER_CREDENTIALS = {"username": "batch13", "password": "12345"}

# Text-to-Speech Function
def speak(text, language='en'):
    engine = pyttsx3.init()
    if language == 'hi' or language == 'ta':  # Set voice for Hindi or Tamil
        voices = engine.getProperty('voices')
        for voice in voices:
            if (language == 'hi' and "Hindi" in voice.name) or (language == 'ta' and "Tamil" in voice.name):
                engine.setProperty('voice', voice.id)
                break
    engine.say(text)
    engine.runAndWait()

# Get Current Time
def get_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}."

# Get Current Date
def get_current_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"The current date is {current_date}."

# Web Search
def web_search(query):
    search_url = f"https://www.bing.com/search?q={query}"
    webbrowser.open(search_url)

# Play YouTube Videos
def play_youtube(video_query):
    youtube_url = f"https://www.youtube.com/results?search_query={video_query}"
    webbrowser.open(youtube_url)

# Open Gmail
def open_gmail():
    gmail_url = "https://mail.google.com/"
    webbrowser.open(gmail_url)

# Tell a Joke
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ]
    return random.choice(jokes)

# Play Music
def play_music(query):
    subprocess.Popen(['spotify', f'search:{query}'])

# Get Weather
def get_weather():
    current_hour = datetime.datetime.now().hour
    if 6 <= current_hour < 18:
        return "The weather is sunny today!"
    else:
        return "The night sky is clear."

# Timer Function
def set_timer(seconds, output_text):
    time.sleep(seconds)
    response = f"The timer is up! {seconds} seconds have passed."
    output_text.set(response)
    speak(response)

# Process Input Function
def process_input(user_input, output_text):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive processing
    response_language = 'en'  # Default response language

    # Tamil Commands
    if "வணக்கம்" in user_input or "ஹலோ" in user_input:  # Hello in Tamil
        response = "வணக்கம்! நான் எப்படி உங்களுக்கு உதவ வேண்டும்?"
        response_language = 'ta'
    elif "நேரம்" in user_input:  # Time in Tamil
        response = get_current_time()
        response_language = 'ta'
    elif "தேதி" in user_input:  # Date in Tamil
        response = get_current_date()
        response_language = 'ta'
    elif "வானிலை" in user_input:  # Weather in Tamil
        response = get_weather()
        response_language = 'ta'
    elif "காமெடி" in user_input:  # Joke in Tamil
        joke = tell_joke()
        response = f"இங்கே ஒரு நகைச்சுவை: {joke}"
        response_language = 'ta'
    elif "பாடல்" in user_input:  # Music in Tamil
        music_query = user_input.replace("பாடல்", "").strip()
        play_music(music_query)
        response = f"Spotifyல் {music_query} பாடலை ஓட வைக்கிறேன்."
        response_language = 'ta'
    elif "தேடல்" in user_input:  # Search in Tamil
        query = user_input.replace("தேடல்", "").strip()
        web_search(query)
        response = f"{query} க்கான தேடல் ஆரம்பிக்கப்பட்டுள்ளது."
        response_language = 'ta'
    elif "யூடியூப்" in user_input:  # YouTube in Tamil
        video_query = user_input.replace("யூடியூப்", "").strip()
        play_youtube(video_query)
        response = f"யூடியூப்பில் {video_query} காணொளிகளை ஓட வைக்கிறேன்."
        response_language = 'ta'
    elif "குட்பை" in user_input or "பிரியாவிடை" in user_input:  # Goodbye in Tamil
        response = "பிரியாவிடை! உங்கள் நாள் நன்றாக அமையட்டும்."
        response_language = 'ta'

    # Hindi Commands
    elif "नमस्ते" in user_input or "हेलो" in user_input:  # Hello in Hindi
        response = "नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?"
        response_language = 'hi'
    elif "सम" in user_input:  # Time in Hindi
        response = get_current_time()
        response_language = 'hi'
    elif "तारीख" in user_input:  # Date in Hindi
        response = get_current_date()
        response_language = 'hi'
    elif "मौसम" in user_input:  # Weather in Hindi
        response = get_weather()
        response_language = 'hi'
    elif "चुटकुला" in user_input:  # Joke in Hindi
        joke = tell_joke()
        response = f"ज़रूर, ये लीजिये एक चुटकुला: {joke}"
        response_language = 'hi'
    elif "गाना" in user_input:  # Music in Hindi
        music_query = user_input.replace("गाना", "").strip()
        play_music(music_query)
        response = f"Spotify पर {music_query} चला रहा हूँ।"
        response_language = 'hi'
    elif "खोज" in user_input:  # Search in Hindi
        query = user_input.replace("खोज", "").strip()
        web_search(query)
        response = f"मैं {query} के लिए खोज कर रहा हूँ।"
        response_language = 'hi'
    elif "यूट्यूब" in user_input:  # YouTube in Hindi
        video_query = user_input.replace("यूट्यूब", "").strip()
        play_youtube(video_query)
        response = f"यूट्यूब पर {video_query} चला रहा हूँ।"
        response_language = 'hi'
    elif "बाय" in user_input or "अलविदा" in user_input:  # Goodbye in Hindi
        response = "अलविदा! आपका दिन शुभ हो।"
        response_language = 'hi'

    # English Commands
    elif "hi" in user_input or "hello" in user_input:
        response = "Hello! How can I help you?"
    elif "time" in user_input:
        response = get_current_time()
    elif "date" in user_input:
        response = get_current_date()
    elif "search" in user_input:
        query = user_input.replace("search", "").strip()
        web_search(query)
        response = f"Searching for {query} on the web."
    elif "youtube" in user_input:
        video_query = user_input.replace("youtube", "").strip()
        play_youtube(video_query)
        response = f"Playing YouTube videos for {video_query}."
    elif "gmail" in user_input:
        open_gmail()
        response = "Opening Gmail. Please sign in."
    elif "joke" in user_input:
        joke = tell_joke()
        response = f"Here's a joke for you: {joke}"
    elif "music" in user_input:
        music_query = user_input.replace("music", "").strip()
        play_music(music_query)
        response = f"Playing music on Spotify for {music_query}."
    elif "weather" in user_input:
        response = get_weather()
    elif "timer" in user_input:
        try:
            seconds = int(user_input.split()[-1])
            threading.Thread(target=set_timer, args=(seconds, output_text)).start()
            response = f"Timer set for {seconds} seconds."
        except ValueError:
            response = "Please provide a valid number for the timer."
    elif "exit" in user_input or "bye" in user_input:
        response = "Goodbye! Have a great day."
    else:
        response = f"I'm sorry, I didn't understand that. How can I assist you?"

    output_text.set(response)
    speak(response, language=response_language)

# Voice Input Function
def listen(output_text, language='en-IN'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        voice_input = recognizer.recognize_google(audio, language=language)
        print(f"You said: {voice_input}")
        output_text.set(f"You said: {voice_input}")
        process_input(voice_input, output_text)
    except sr.UnknownValueError:
        response = "I didn't catch that. Please try again."
        output_text.set(response)
        speak(response, language=language.split('-')[0])
    except sr.RequestError:
        response = "Sorry, I'm having trouble connecting to the service."
        output_text.set(response)
        speak(response, language=language.split('-')[0])

m

# Main Assistant Function
def main():
    root = tk.Tk()
    root.title("Virtual Assistant")

    # Center Window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width, window_height = 800, 600
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.configure(bg="#F0F0F0")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font=("Arial", 16), padding=10, width=20, background="#4CAF50", foreground="white", relief="flat")
    style.configure("TLabel", font=("Arial", 16), background="#98FF98", foreground="#333")
    style.configure("TEntry", font=("Arial", 14), padding=10)

    frame = ttk.Frame(root, padding=20, style="TFrame")
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    input_label = ttk.Label(frame, text="You:", anchor="e")
    input_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    input_entry = ttk.Entry(frame, font=("Arial", 14), width=50)
    input_entry.grid(row=0, column=1, padx=10, pady=10)

    output_text = tk.StringVar()
    output_label = ttk.Label(frame, textvariable=output_text, wraplength=700, anchor="w")
    output_label.grid(row=1, column=0, columnspan=2, pady=20)

    # Set grid column and row weights to make the layout responsive
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=3)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_rowconfigure(3, weight=1)
    frame.grid_rowconfigure(4, weight=1)
    frame.grid_rowconfigure(5, weight=1)

    text_button = ttk.Button(frame, text="🔎Text Search", command=lambda: threading.Thread(target=process_input, args=(input_entry.get(), output_text)).start())
    text_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

    voice_button = ttk.Button(frame, text="🎙️Voice Search(EN)", command=lambda: threading.Thread(target=listen, args=(output_text, 'en-IN')).start())
    voice_button.grid(row=3, column=0, pady=10, sticky="ew")

    hindi_voice_button = ttk.Button(frame, text="🎙️Voice Search(HI)", command=lambda: threading.Thread(target=listen, args=(output_text, 'hi-IN')).start())
    hindi_voice_button.grid(row=3, column=1,columnspan=3, pady=10,sticky="ew" )

    tamil_voice_button = ttk.Button(frame, text="🎙️Voice Search(TA)", command=lambda: threading.Thread(target=listen, args=(output_text, 'ta-IN')).start())
    tamil_voice_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    exit_button = ttk.Button(frame, text="Exit", command=root.destroy)
    exit_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

    root.mainloop()

if __name__ == "__main__":
    login_page()
