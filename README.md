
# **Jarvis - Voice Assistant**

## **Overview**

Jarvis is a voice-activated assistant built using Python. It can perform various tasks such as answering questions using OpenAI's GPT-3, playing music, opening websites, and sending emails. The assistant is powered by several Python libraries, including `pyttsx3` for text-to-speech, `speech_recognition` for voice input, and `wikipedia` for information retrieval.

## **Features**

- **Voice Interaction**: Jarvis listens to voice commands and responds with speech.
- **OpenAI Integration**: Jarvis uses GPT-3 to answer user queries in natural language.
- **Task Automation**: Perform tasks such as opening websites, playing music, and sending emails.
- **Email Functionality**: Jarvis can send emails to specified recipients using Gmail.

## **Technologies Used**

- Python 3.x
- `pyttsx3`: Text-to-speech conversion
- `speech_recognition`: Converts speech to text
- `openai`: OpenAI's GPT-3 for intelligent responses
- `wikipedia`: Wikipedia API for querying information
- `smtplib`: Sending emails using Gmail's SMTP server
- `webbrowser`: Opening websites
- `os`: Interacting with the operating system

## **Installation**

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/jarvis-voice-assistant.git
    ```

2. Install the required libraries:

    ```bash
    pip install openai pyttsx3 speechRecognition wikipedia
    ```

3. Set up your OpenAI API key by replacing `'your_openai_api_key'` with your actual API key.

4. Replace the placeholders for your Gmail credentials (`your-email@gmail.com` and `your-password`) in the `sendEmail` function with your actual credentials.

## **Usage**

1. Run the `jarvis.py` script:

    ```bash
    python jarvis.py
    ```

2. The assistant will greet you based on the time of the day and wait for voice commands.

3. **Voice Commands**:
    - **"wikipedia <query>"**: Searches Wikipedia for the given query.
    - **"open youtube"**: Opens YouTube in the browser.
    - **"open google"**: Opens Google in the browser.
    - **"open stackoverflow"**: Opens Stack Overflow in the browser.
    - **"play music"**: Plays music from the specified directory.
    - **"the time"**: Tells the current time.
    - **"open code"**: Opens Visual Studio Code.
    - **"email to satyam"**: Sends an email to `satyamkumarg089@gmail.com`. Jarvis will ask you what to say.

## **Example Commands**

- "What is the capital of France?"
- "Open Google"
- "Play music"
- "Send an email to Satyam"

## **Contributions**

Feel free to fork the repository and submit pull requests for new features, bug fixes, or improvements!

## **License**

This project is open-source and available under the MIT License.
