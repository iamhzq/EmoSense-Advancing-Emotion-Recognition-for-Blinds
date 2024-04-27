'''
emotion_audio_mapping = {
    "happy": "You look happy!",
    "sad": "I sense sadness.",
    "angry": "I detect anger.",
    "neutral": "You seem neutral.",
    "disgust": "You are disgusted?"
    # Add more emotions and audio messages as needed
}

from gtts import gTTS
import tempfile
import os

def generate_audio_based_on_emotion(detected_emotion):
    # Lookup the corresponding audio message
    audio_message = emotion_audio_mapping.get(detected_emotion, "I can't identify your emotion.")
    
    # Generate audio from the audio message using gTTS
    tts = gTTS(text=audio_message, lang='en')  # 'en' stands for English; change it as needed
    
    # Create a temporary audio file
    audio_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    audio_path = audio_file.name
    tts.save(audio_path)

    return audio_path

# Example usage
detected_emotion = "happy"  # Replace with the detected emotion from your model
audio_path = generate_audio_based_on_emotion(detected_emotion)

# You can play the audio using a suitable library or application
os.system(f"mp3 {audio_path}")  # Replace 'mpg321' with a compatible player
'''

import pyttsx3
text_speech = pyttsx3.init()
answer = input("What you want to convert to speech?")
text_speech.say(answer)
text_speech.runAndWait()
