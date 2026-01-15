import sounddevice as sd
import soundfile as sf
import uuid


def listen_microphone():
    """
    Запись голоса с микрофона.
    """

    duration = 5  # секунд
    samplerate = 16000
    filename = f"temp_{uuid.uuid4()}.wav"

    print("Слушаю...")

    try:
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
        sd.wait()
        sf.write(filename, audio, samplerate)
        return filename
    except Exception as e:
        print(f"Ошибка записи: {e}")
        return None
