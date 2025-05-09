import speech_recognition as sr

def live_record_and_save(output_file):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Adjusting for ambient noise... Please wait.")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Start speaking. Press Ctrl+C to stop.")

        with open(output_file, 'w') as f:
            try:
                while True:
                    print("Listening...")
                    audio = recognizer.listen(source)
                    try:
                        text = recognizer.recognize_google(audio)
                        print("You said:", text)
                        f.write(text + '\n')
                    except sr.UnknownValueError:
                        print("Could not understand the audio.")
                    except sr.RequestError as e:
                        print(f"API error: {e}")
            except KeyboardInterrupt:
                print("\nRecording stopped. Transcription saved to", output_file)

if __name__ == "__main__":
    output_path = "transcription_output.txt"
    live_record_and_save(output_path)
