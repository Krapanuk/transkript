import whisper
import subprocess
import os

def vimeo_to_text(vimeo_url, output_text="transcript.txt", temp_audio="temp_audio.mp3"):
    """
    Konvertiert Vimeo-Video zu Textdatei
    """
    try:
        # Schritt 1: Audio von Vimeo herunterladen
        print("Lade Audio von Vimeo herunter...")
        cmd = [
            "yt-dlp",
            "-x",
            "--audio-format", "mp3",
            "--output", temp_audio,
            vimeo_url
        ]
        subprocess.run(cmd, check=True)
        
        # Schritt 2: Whisper-Modell laden
        print("Lade Whisper-Modell...")
        model = whisper.load_model("base")
        
        # Schritt 3: Audio transkribieren
        print("Transkribiere Audio...")
        result = model.transcribe(temp_audio)
        
        # Schritt 4: Text in Datei speichern
        with open(output_text, 'w', encoding='utf-8') as f:
            f.write(result["text"])
        
        # Temporäre Audiodatei löschen
        os.remove(temp_audio)
        
        print(f"Transkription erfolgreich in {output_text} gespeichert!")
        return result["text"]
        
    except Exception as e:
        print(f"Fehler: {e}")
        return None

# Verwendung
vimeo_url = "https://vimeo.com/514283044"
transcript = vimeo_to_text(vimeo_url)
