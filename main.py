import os
import time
from openai import OpenAI
from settings import settings
import transcribe_audio
from process_folder import process_folder


def main():
    client = OpenAI(
        api_key=settings.api.api_key
    )

    start_time = time.time()

    t_audio = transcribe_audio.transcribe_audio("KSE Macro - Group 11 - Reducing Labor Migration and Encouraging Ukrainian Refugees to Return Post-War.mp3", client)
    print(t_audio)
    finish_time = time.time()
    print(f"wait time: {finish_time - start_time}")
    # print(key_pointer(t_audio))


if __name__ == "__main__":
    main()

# finish_time = time.time()
# print(f"working time: {finish_time - start_time}")   # 30 sec audio +- 10 sec wait time


# def abstract_summary_extraction(transcription):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a highly skilled AI trained in language comprehension and summarization. "
#                            "I would like you to read the following text and summarize it into a concise abstract paragraph."
#                            "Aim to retain the most important points, providing a coherent and readable summary "
#                            "that could help a person understand the main points of the discussion without needing to read the entire text."
#                            "Please avoid unnecessary details or tangential points. "
#             },
#             {
#                 "role": "user",
#                 "content": transcription
#             }
#         ]
#     )
#     return response.choices[0].message.content


# def key_pointer(transcription):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "Please distill the key arguments and or facts from this text."
#                            " Return a bullet point list with one - two sentences per point."
#             },
#             {
#                 "role": "user",
#                 "content": transcription
#             }
#         ]
#     )
#     return response.choices[0].message.content
# #
# #
# print(key_pointer(transcribe_audio))
