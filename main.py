import os
from openai import OpenAI
from settings import settings

client = OpenAI(
    api_key=settings.api.api_key
)


def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        try:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
            return transcription.text
        except Exception as e:
            return str(e)


print(transcribe_audio("video1.mp3"))
