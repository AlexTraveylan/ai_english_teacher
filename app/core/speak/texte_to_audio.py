from pathlib import Path

from openai import OpenAI
from pydub import AudioSegment
from pydub.playback import play

from app.settings import OPENAI_API_KEY, RECORDING_DIR


def create_audio_from_text(text: str, file_path: Path) -> Path:
    """Crée un fichier audio à partir d'un texte."""

    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )

    response.stream_to_file(file_path)

    return file_path


def play_audio(file_path: Path) -> None:
    """Joue un fichier audio."""

    audio = AudioSegment.from_file(file_path, format="mp3")

    # Jouez l'audio
    play(audio)


if __name__ == "__main__":
    # text = "Hello, my name is John. I am a software engineer."
    file_path = RECORDING_DIR / "hello_world.mp3"
    # create_audio_from_text(text, file_path)

    play_audio(file_path)
