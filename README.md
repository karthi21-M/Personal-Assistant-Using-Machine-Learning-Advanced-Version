This is a simple virtual assistant that can perform various tasks like telling the time, date, weather, playing music, searching the web, telling jokes, and much more.
The assistant can interact with users via both text and voice commands in three languages: English, Hindi, and Tamil.

Features:
Login Page: Requires username and password to access the assistant.
Voice Commands: Supports voice input for commands in English, Hindi, and Tamil.
Text-to-Speech: Provides voice responses based on user input in the respective language.
Multilingual Support: Recognizes and responds to commands in English, Hindi, and Tamil.
Various Tasks:
Get Current Time
Get Current Date
Weather Information
Tell Jokes
Play Music (via Spotify)
Open Gmail
Web Search
YouTube Search
Set Timer
Exit the Assistant
Prerequisites
Before you run the assistant, you need to install a few Python libraries.

pyttsx3 (Text-to-Speech conversion)
speech_recognition (Voice input recognition)
webbrowser (To open URLs in a browser)
subprocess (For executing commands like opening Spotify)
tkinter (For the graphical user interface)
random (For generating random jokes)
time (For timers and delays)
datetime (For fetching current time and date)
You can install the required libraries using pip:

bash
Copy code
pip install pyttsx3 SpeechRecognition
tkinter is usually bundled with Python, so no separate installation is needed.

How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/virtual-assistant.git
cd virtual-assistant
Run the main script:

bash
Copy code
python assistant.py
Login:

The assistant will prompt you for a username and password.
Default credentials:
Username: batch13
Password: 12345
Interact with the Assistant:

Once logged in, you can use either text input or voice input to interact with the assistant.
You can click on the text box and enter your commands, or click on one of the voice search buttons to speak your command.
Voice Command Languages:

The assistant supports voice commands in:

English (EN)
Hindi (HI)
Tamil (TA)
For example:

"What is the time?" (English)
"समय क्या है?" (Hindi)
"நேரம் என்ன?" (Tamil)
Exit the Assistant:

Click the Exit button to close the assistant.
Commands Supported
English:
time: Get the current time.
date: Get the current date.
weather: Get weather information.
joke: Tell a random joke.
search [query]: Search the web for a query.
youtube [query]: Search for a video on YouTube.
gmail: Open Gmail.
music [song name]: Play music on Spotify.
exit or bye: Exit the assistant.
Hindi:
समय: Get the current time.
तारीख: Get the current date.
मौसम: Get weather information.
चुटकुला: Tell a random joke.
खोज [query]: Search the web for a query.
यूट्यूब [query]: Search for a video on YouTube.
गाना [song name]: Play music on Spotify.
गमेल: Open Gmail.
बाय or अलविदा: Exit the assistant.
Tamil:
நேரம்: Get the current time.
தேதி: Get the current date.
வானிலை: Get weather information.
காமெடி: Tell a random joke.
தேடல் [query]: Search the web for a query.
யூடியூப் [query]: Search for a video on YouTube.
பாடல் [song name]: Play music on Spotify.
குட்பை or பிரியாவிடை: Exit the assistant.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Feel free to fork the project, submit issues, or create pull requests with improvements. Contributions are welcome!
