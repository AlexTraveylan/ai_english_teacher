""" This module contains the code to convert audio to text using OpenAI's API. """

from openai import OpenAI

from app.settings import OPENAI_API_KEY, RECORDING_DIR


def audio_to_text(audio_file_path: str) -> str:
    """Converts an audio file to text."""

    client = OpenAI(api_key=OPENAI_API_KEY)

    audio_file = open(audio_file_path, "rb")
    transcript = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        response_format="verbose_json",
        timestamp_granularities=["word"],
    )

    return " ".join([word["word"] for word in transcript.words])


if __name__ == "__main__":
    file = RECORDING_DIR / "hello_world.mp3"
    text = audio_to_text(file)
    print(text)
