from pydub import AudioSegment


def split_audio(input_file, start_time, end_time, output_file):
    """
    Splits an audio file into a subclip.

    Parameters:
    input_file (str): The path to the input audio file.
    start_time (int): The start time in milliseconds from which to begin the clip.
    end_time (int): The end time in milliseconds at which to end the clip.
    output_file (str): The path to save the output audio file.
    """
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Extract the subclip
    subclip = audio[start_time:end_time]

    # Export the subclip to a new file
    subclip.export(output_file, format="mp3")


# Example usage
input_audio = "UKR.mp3"
start_minute = 6  # Start at 1 minute
end_minute = 64  # End at 2 minutes

# Convert minutes to milliseconds
start_time = start_minute * 60 * 1000
end_time = end_minute * 60 * 1000

output_audio = "UKR_trimered.mp3"

split_audio(input_audio, start_time, end_time, output_audio)
