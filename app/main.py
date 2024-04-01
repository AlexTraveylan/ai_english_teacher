from enum import StrEnum, auto

from app.core.think.text_to_response import MessageAi
from app.settings import RECORDING_DIR


class State(StrEnum):
    RECORDING = auto()
    TRANSLATING = auto()
    THINKING = auto()
    SPEAKING = auto()


def main():

    from app.core.listen.audio_to_file import record_audio

    print(State.RECORDING)
    # Enregistrez la voix de l'utilisateur
    input_voice = RECORDING_DIR / "input.wav"
    record_audio(input_voice)

    from app.core.translate_audio_to_text.audio_to_text import audio_to_text

    print(State.TRANSLATING)
    # Convertir la voix en texte
    input_text = audio_to_text(input_voice)

    from app.core.think.text_to_response import completion

    print(State.THINKING)
    # Obtenir une réponse à partir du texte
    systeme = MessageAi(
        role="system",
        content="You are an english teacher and you have to have a conversation with a student.",
    )
    user = MessageAi(role="user", content=input_text)
    answer = completion(messages=[systeme, user])

    from app.core.speak.texte_to_audio import create_audio_from_text, play_audio

    print(State.SPEAKING)
    # Convertir le texte en audio
    output_voice = RECORDING_DIR / "output.mp3"
    create_audio_from_text(answer, output_voice)

    # Jouer l'audio
    play_audio(output_voice)


if __name__ == "__main__":
    main()
