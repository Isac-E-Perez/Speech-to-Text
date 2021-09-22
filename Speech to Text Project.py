import speech_recognition as sr  # importing SpeechRecognition library

# going to be using Google Speech Recognition (doesn't require any API key)

filename = "Isac.wav"  # need .wav (cannot use m4a or m4p)

# initialize the recognizer

root = sr.Recognizer()

# loading file -> converting the speech into text using Google Speech Recognition

with sr.AudioFile(filename) as source:  # open the file
    audio_data = root.record(source)  # listen for the data (load audio to memory)
    text = root.recognize_google(audio_data)  # performs speech recognition on audio_data (convert from speech to text)
    print(text)
