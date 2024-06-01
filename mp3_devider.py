import os
from pydub import AudioSegment


def divide_mp3(input_file, output_folder, num_parts):
    audio = AudioSegment.from_mp3(input_file)
    total_duration = len(audio)
    part_duration = total_duration // num_parts
    start_time = 0

    for i in range(num_parts):
        end_time = start_time + part_duration

        if i == num_parts - 1:
            end_time = total_duration

        audio_part = audio[start_time:end_time]
        output_file = os.path.join(output_folder, f"part{i + 1}.mp3")
        audio_part.export(output_file, format="mp3")
        start_time = end_time


def process_folder(input_folder):
    output_folder = input_folder + "_divided"
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            input_file = os.path.join(input_folder, filename)
            file_size_mb = os.path.getsize(input_file) / (1024 * 1024)  # Convert bytes to megabytes

            if file_size_mb <= 25:
                output_file = os.path.join(output_folder, filename)
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
                    f_out.write(f_in.read())
            else:
                file_output_folder = os.path.join(output_folder, os.path.splitext(filename)[0])
                os.makedirs(file_output_folder, exist_ok=True)
                if file_size_mb <= 49:
                    divide_mp3(input_file, file_output_folder, num_parts=2)
                elif file_size_mb <= 100:
                    divide_mp3(input_file, file_output_folder, num_parts=5)
                else:
                    divide_mp3(input_file, file_output_folder, num_parts=10)

    print(f"All MP3 files in the folder '{input_folder}' have been processed and saved in the folder: {output_folder}")


divide_mp3("444.mp3", "4", 2)

# Example usage
# input_folder = "set4_mp3"
# process_folder(input_folder)
