# 🤖 Jarvis - Python-Voice-Assistant
Jarvis is a Python-based voice assistant that can perform various tasks like opening applications, searching the web, telling jokes, fetching news, checking system status, and more — all through voice commands.

## 📑 Table of Contents

- [Jarvis - Python Voice Assistant](#-jarvis---python-voice-assistant)
- [Features](#-features)
- [Technologies Used](#️-technologies-used)
- [Installation](#-installation)
- [Usage](#️-usage)
- [Important Notes](#️-important-notes)
- [Security Warning](#-security-warning)
- [Project Structure](#-project-structure)
- [Future Improvements](#-future-improvements)  
- [Demo](#-demo)

## Features
- Voice recognition using speech input  
- Text-to-speech responses  
- Open websites (YouTube, Google, Facebook, Instagram)  
- Wikipedia search  
- Weather & temperature updates  
- Latest tech news  
- Play music on YouTube  
- Tell jokes  
- Open system applications (CMD, Notepad, VS Code)  
- System controls (shutdown, restart, logout)  
- Battery status monitoring  
- Take screenshots  
- Keyboard automation (task manager, window switch, etc.)  

## Technologies Used

- Python 🐍  
- SpeechRecognition  
- pyttsx3 (Text-to-Speech)  
- pywhatkit  
- pyautogui  
- BeautifulSoup  
- psutil  
- requests  
- wikipedia  
- and more...  

## Installation

- Clone the repository:  
    git clone https://github.com/MohammadKhalandar39/jarvis-voice-assistant.git  
    cd jarvis-voice-assistant  

- Install dependencies:  
   pip install -r requirements.txt

## Usage

Run the script:  
               python jarvis.py  
Then say:  
- "Jarvis" → to activate  
- "Open YouTube"  
- "Play [song name]"  
- "Tell me a joke"  
- "Shutdown the system"  

## Important Notes
- Requires a working microphone  
- Optimized for Windows (uses system-specific commands)  
- API keys (if any) should be kept secure and not exposed publicly  
- Internet connection is required for many features  

## Security Warning
Your project currently contains an API key inside the code.  
It is strongly recommended to:  
- Remove it from the source code  
- Use environment variables instead  

## Project Structure
jarvis.py        # Main voice assistant script
README.md        # Project documentation

## Future Improvements  
- Add GUI interface  
- Support for multiple languages  
- Integration with AI APIs  
- Better error handling  
- Cross-platform compatibility  

## 🎥 Demo  
![Jarvis Demo](assets/demo.gif)  







