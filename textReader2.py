import pyttsx3

def speak_text():
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Set speaking rate (default ~200)
    engine.setProperty('rate', 175)

    # Set voice (0 for male, 1 for female — depends on your system)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # change to voices[0] for male

    print("Welcome to TextReader!")
    print("Type something and I’ll read it out loud.")
    print("Type 'exit' to stop.\n")

    while True:
        text = input("Enter text: ")
        if text.lower() == 'exit':
            print("Goodbye!")
            break
        if text.strip() == "":
            print("⚠️  Please enter some text.")
            continue

        # Speak the entered text
        engine.say(text)
        engine.runAndWait()
        print("✅  Done speaking!\n")

if __name__ == "__main__":
    speak_text()
