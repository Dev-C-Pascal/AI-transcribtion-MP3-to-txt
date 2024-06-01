from pydub import AudioSegment


def convert_aac_to_mp3(input_file, output_file):
    # Load the AAC file
    audio = AudioSegment.from_file(input_file, format="aac")

    # Export as MP3
    audio.export(output_file, format="mp3")
    print(f"Conversion successful: {output_file}")


# Example usage
input_file = "333.aac"
output_file = "333.mp3"
convert_aac_to_mp3(input_file, output_file)