import whisper
import sounddevice as sd
import numpy as np
import tempfile
import os
from scipy.io.wavfile import write

model = whisper.load_model("small") # Alternativen: tiny, base, small, medium, large

def record_audio(duration=10, sample_rate=16000, device_index=0):
    #print(sd.query_devices())
    print("Starte Aufnahme...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, device=device_index)
    sd.wait()
    return audio, sample_rate

def transcribe(audio_data, sample_rate):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        write(tmp.name, sample_rate, (audio_data * 32767).astype(np.int16))
        tmp_path = tmp.name

    # Transkription außerhalb des Datei-Kontexts durchführen:
    result = model.transcribe(tmp_path, fp16=False)

    # Datei nach abgeschlossener Transkription löschen:
    os.unlink(tmp_path)

    return result["text"]


with open("transkript.txt", "a", encoding="utf-8") as file:
    try:
        while True:
            audio_data, sr = record_audio()
            transcription = transcribe(audio_data, sr)
            print("Transkription:", transcription)
            file.write(transcription + "\n")
    except KeyboardInterrupt:
        print("Beendet durch Benutzer.")