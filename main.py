import os
import time
from openai import OpenAI
from settings import settings
import transcribe_audio
import process_folder


# from key_pointer import key_pointer


def main():
    client = OpenAI(api_key=settings.api.api_key)
    # res = process_folder.process_folder("1", client)
    res = transcribe_audio.transcribe_audio("1.mp3", client)

    print(res)

if __name__ == "__main__":
    start_time = time.time()
    main()

    finish_time = time.time()
    print(f"wait time: {finish_time - start_time}")

# 30 sec audio +- 10 sec wait time


# client = OpenAI(api_key=settings.api.api_key)
#
# response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": },
#     {"role": "user", "content": "Who won the world series in 2020?"},
#   ]
#
#
# )
# print(response.choices[0].message.content)
