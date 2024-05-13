import os
import time
import subprocess
from pydub import AudioSegment


def convert_mp4_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_file
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully converted mp4 to mp3")
    except subprocess.CalledProcessError as e:
        print(e.output)
        print("Could not convert mp4 to mp3")


# convert_mp4_to_mp3()


def convert_m4a_to_mp3(m4a_file, mp3_file):
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    audio.export(mp3_file, format="mp3")


convert_m4a_to_mp3("Berlinska in Chicago.m4a","Berlinska_Chicago.mp3")


def convert_folder(input_folder):
    output_folder = input_folder + "_mp3"
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp3")

        if filename.endswith(".mp4"):
            convert_mp4_to_mp3(input_file, output_file)
        elif filename.endswith(".m4a"):
            convert_m4a_to_mp3(input_file, output_file)

    return output_folder


# start_time = time.time()
# input_folder = "set4"
# output_folder = convert_folder(input_folder)
# print(f"Conversion complete. Output folder: {output_folder}")
# finish_time = time.time()
# print(f"Execution time: {finish_time - start_time}")