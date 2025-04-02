import whisper
import sounddevice as sd
import wave
import tempfile
import os
from scipy.io.wavfile import write

# Whisper-Modell laden
model = whisper.load_model("base")  # Alternativen: tiny, base, small, medium, large

# Parameter
DURATION = 10  # Dauer der segmentierten Aufnahmen in Sekunden
DEVICE_INDEX = 1  # Index des Aufnahmegeräts

# Durchgehende Aufnahmedatei initialisieren
continuous_audio_path = "continuous.wav"
continuous_wavefile = wave.open(continuous_audio_path, 'wb')
device_info = sd.query_devices(DEVICE_INDEX, 'input')
sample_rate = int(device_info['default_samplerate'])
continuous_wavefile.setnchannels(1)
continuous_wavefile.setsampwidth(2)
continuous_wavefile.setframerate(sample_rate)

def record_audio(duration=DURATION, device_index=DEVICE_INDEX):
    print("Starte segmentierte Aufnahme...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16', device=device_index)
    sd.wait()
    # Durchgehende Aufnahme speichern
    continuous_wavefile.writeframes(audio.tobytes())
    return audio, sample_rate

def transcribe(audio_data, sample_rate):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        write(tmp.name, sample_rate, audio_data)
        tmp_path = tmp.name

    # Transkription durchführen
    result = model.transcribe(tmp_path, fp16=False)

    # Temporäre Datei löschen
    os.unlink(tmp_path)

    return result["text"]

try:
    with open("transkript.txt", "a", encoding="utf-8") as file:
        while True:
            audio_data, sr = record_audio()
            transcription = transcribe(audio_data, sr)
            print("Transkription:", transcription)
            file.write(transcription + "\n")
except KeyboardInterrupt:
    print("Beendet durch Benutzer.")
finally:
    continuous_wavefile.close()
    print(f"Durchgehende Aufnahme gespeichert unter: {continuous_audio_path}")