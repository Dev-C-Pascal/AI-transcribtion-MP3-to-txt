import os
import time
from openai import OpenAI
from settings import settings
from transcribe_audio import transcribe_audio
from process_folder import process_folder
from key_pointer import key_pointer


def main():
    client = OpenAI(api_key=settings.api.api_key)

    input_folder = "set4_mp3_divided"
    inpt_folder = process_folder(input_folder, client)
    print(inpt_folder)


    # inpt_folder = input("Berlin_transcripted")
    # for file_path in inpt_folder:
    #     with open(file_path, 'r') as file:
    #         transcription = file.read()
    #         key_points = key_pointer(transcription, client)
    #         print(f"Key points for {file_path}:")
    #         print(key_points)


if __name__ == "__main__":
    start_time = time.time()
    main()

    finish_time = time.time()
    print(f"wait time: {finish_time - start_time}")

# 30 sec audio +- 10 sec wait time
