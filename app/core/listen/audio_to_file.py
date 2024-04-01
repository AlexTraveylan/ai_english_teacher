import wave
from pathlib import Path

import pyaudio

# Paramètres de l'enregistrement
FORMAT = pyaudio.paInt16  # Format des données audio (16 bits PCM)
CHANNELS = 1  # Mono
RATE = 44100  # Taux d'échantillonnage
CHUNK = 1024  # Taille des blocs de lecture
RECORD_SECONDS = 5  # Durée de l'enregistrement
WAVE_OUTPUT_FILENAME = (
    "app/core/audio_in/records/output.wav"  # Nom du fichier de sortie
)


def record_audio(file_path: Path | str) -> Path:
    """Enregistre un fichier audio au chemin spécifié."""

    file_path = Path(file_path)

    # Initialisation de l'interface PyAudio
    audio = pyaudio.PyAudio()

    # Ouverture du flux d'enregistrement
    stream = audio.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    print("Enregistrement en cours...")

    frames = []

    # Boucle d'enregistrement
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Enregistrement terminé.")

    # Arrêt du flux
    stream.stop_stream()
    stream.close()

    # Fermeture de l'interface PyAudio
    audio.terminate()

    # Sauvegarde du fichier .wav
    wf = wave.open(str(file_path), "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

    print(f"Fichier '{file_path}' sauvegardé avec succès.")

    return file_path


if __name__ == "__main__":
    record_audio(WAVE_OUTPUT_FILENAME)
