# 🔊 Voice Assistant using Python

A powerful voice-controlled assistant built with Python that use to answer deep questions, tell jokes, fetch the weather, solve math problems, play music, and much more. This is your own mini Jarvis ✨.

---

## 🚀 Features

| Command Example                     | Functionality                               |
|------------------------------------|---------------------------------------------|
| "Play Faded by Alan Walker"        | Plays song on YouTube                       |
| "What time is it?"                 | Tells current time                          |
| "What is quantum computing?"       | Answers using Gemini AI                     |
| "Tell me a joke"                   | Says a random joke                          |
| "Who is Elon Musk?"                | Gives short info from Wikipedia             |
| "What is 12 plus 6?"               | Calculates math expression                  |
| "What’s the weather in Delhi?"     | Provides weather update from OpenWeatherMap |

---

## 📊 Tech Stack

- Python 3.7+
- [Google Gemini API](https://ai.google.dev)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Pyttsx3](https://pypi.org/project/pyttsx3/)
- [PyWhatKit](https://pypi.org/project/pywhatkit/)
- [Wikipedia](https://pypi.org/project/wikipedia/)
- [PyJokes](https://pypi.org/project/pyjokes/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [google-generativeai](https://pypi.org/project/google-generativeai/)

---

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes requests google-generativeai
```

### 3. Set Up API Keys

#### 🔐 Google Gemini API
- Go to [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
- Generate a new API key
- Replace it in your script:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

#### 🔐 OpenWeatherMap API
- Create an account on [https://openweathermap.org/api](https://openweathermap.org/api)
- Replace the API key in your script:

```python
owm = OWM('YOUR_WEATHER_API_KEY')
```

---

## ▶️ Run the Project

```bash
python main.py
```

Once the assistant is listening, speak any command and watch it do the magic!

---

## 🚪 Example Commands

Try saying:
- "Play Believer on YouTube"
- "What is 56 plus 44?"
- "Who is the president of the US?"
- "What’s the weather in Mumbai?"
- "Tell me a fun fact"
- "Explain gravity in simple words"

---

## 🌈 Customize It

You can modify and extend this assistant to:
- Add a GUI using Tkinter or PyQt
- Add email sending & reading capabilities
- Store notes and reminders
- Support multiple languages
- Save user preferences or chat history

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Credits

Built with ❤️ by [Your Name]. Powered by Google Gemini and Python open-source libraries.

Want to contribute? Fork the repo and submit a PR 🚀

---

## 📊 Screenshots (Optional)

> Add screenshots or gifs of the project running if available

---

## 🔍 Troubleshooting

- **Gemini API Quota Error?** Check your usage here: https://makersuite.google.com
- **Microphone not working?** Try using a different audio input device or reinstall `pyaudio`
- **Weather not showing?** Make sure the city name is correctly spelled and your API key is valid

---

## 🚀 Bonus Ideas

- Add face recognition (OpenCV)
- Translate spoken words to other languages
- Create a chatbot web app using Flask or Streamlit

---


