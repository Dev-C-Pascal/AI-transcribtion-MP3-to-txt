import os
from typing import Any, Dict

import transcribe_audio


def _format_transcription_output(
    transcription: Dict[str, Any], use_timestamps: bool, interval_seconds: int
) -> str:
    if not isinstance(transcription, dict):
        return str(transcription)

    if transcription.get("error"):
        return str(transcription["error"])

    if use_timestamps:
        formatted = transcribe_audio.format_segments_with_timestamps(
            transcription.get("segments", []), interval_seconds=interval_seconds
        )
        if formatted:
            return "\n\n".join(formatted)

    return transcription.get("text", "")


def process_folder(
    input_folder, client, *, use_timestamps: bool = False, interval_seconds: int = 5
):
    output_folder = input_folder + "_transcripted"
    os.makedirs(output_folder, exist_ok=True)

    for item in os.listdir(input_folder):
        item_path = os.path.join(input_folder, item)
        if os.path.isdir(item_path):
            # Item is a subfolder
            output_subfolder = item + "_transcripted"
            output_subfolder_path = os.path.join(output_folder, output_subfolder)
            os.makedirs(output_subfolder_path, exist_ok=True)

            for filename in os.listdir(item_path):
                if filename.endswith(".mp3"):
                    input_file_path = os.path.join(item_path, filename)
                    transcription = transcribe_audio.transcribe_audio(
                        input_file_path, client
                    )
                    output_text = _format_transcription_output(
                        transcription, use_timestamps, interval_seconds
                    )
                    output_filename = os.path.splitext(filename)[0] + "_transcripted.txt"
                    output_file_path = os.path.join(output_subfolder_path, output_filename)
                    with open(output_file_path, 'w') as output_file:
                        output_file.write(output_text)

        elif item.endswith(".mp3"):
            input_file_path = os.path.join(input_folder, item)
            transcription = transcribe_audio.transcribe_audio(input_file_path, client)
            output_text = _format_transcription_output(
                transcription, use_timestamps, interval_seconds
            )
            output_filename = os.path.splitext(item)[0] + "_transcripted.txt"
            output_file_path = os.path.join(output_folder, output_filename)
            with open(output_file_path, 'w') as output_file:
                output_file.write(output_text)

    print(f"Transcription complete. Results saved in the folder: {output_folder}")
