import pyttsx3

def speak_text():
    print("Welcome to TextReader!")
    print("Type something and I’ll read it out loud.")
    print("Type 'exits' to stop.\n")

    while True:
        text = input("Enter text: ")
        if text.lower().strip() == 'exit':
            print("Goodbye!")
            break
        if not text.strip():
            print("⚠️ Please enter some text.")
            continue

        # Reinitialize engine each time to fix multi-speak issue
        engine = pyttsx3.init()
        engine.setProperty('rate', 175)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Male voice; change to 1 for female

        engine.say(text)
        engine.runAndWait()
        engine.stop()  # ensures engine resets properly

        print("✅ Done speaking!\n")

if __name__ == "__main__":
    speak_text()
