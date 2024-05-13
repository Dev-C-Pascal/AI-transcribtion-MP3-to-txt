def key_pointer(transcription, client):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Please distill the key arguments and or facts from this text."
                           " Return a bullet point list with one - two sentences per point."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response.choices[0].message.content