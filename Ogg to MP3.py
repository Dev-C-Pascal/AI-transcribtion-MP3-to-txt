import ffmpeg


def convert_ogg_to_mp3(ogg_file_path, mp3_file_path):
    try:
        # Convert the OGG file to MP3 using ffmpeg
        ffmpeg.input(ogg_file_path).output(mp3_file_path).run()
        print(f"Conversion complete: {ogg_file_path} to {mp3_file_path}")
    except ffmpeg.Error as e:
        print(f"Error during conversion: {e.stderr.decode()}")


# Example usage

# Example usage
ogg_file = "2.ogg"
mp3_file = "2.mp3"
convert_ogg_to_mp3(ogg_file, mp3_file)
