def transcribe_audio(audio_file_path, client):
    with open(audio_file_path, 'rb') as audio_file:
        try:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
            return transcription.text
        except Exception as e:
            return str(e)
