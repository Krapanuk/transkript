# Transkript

Mit der transcribe.py ist es möglich, sich mit lokaler KI, ohne, dass Daten das eigene System verlassen, Meetings, Videos, ..., jeglichen gesprochenen Text in die Textdatei transkript.txt zu transkribieren.

Mit
* transcribe.py
  wird aus dem im System ankommenden Audio der Text sowohl
  * durchgängig in eine continuous.wav geschrieben, um später mit transcribe_audio.py "en block" extrahiert zu werden, also auch
  * schrittweise in 10-Sek.-Abschnitten iterativ transkribiert und "häppchenweise" in eine transkript.txt geschrieben
* youtube_download_mp4.py\
  kann der Ton des kompletten YouTube-Videos als mp4 lokal gespeichert werden, um danach transkribiert zu werden mit
* transcribe_audio.py\
  kann den in der im Code genannten Audiodatei in eine transkript_full.txt transkribieren.
* vimeoToText.py\
  kann das im Code via vimeo_url referenzierte Vimeo-Video direkt in Text umwandeln.

# Vorbereitungen

Um die Skripte nutzen zu können sind vorab folgende Dinge zu tun:

## Repo clonen
* Dieses git repo clonen und 
* virtuelle-Umgebung aktivieren via
  * python -m venv venv
  * venv\Scripts\activate

## FFmpeg herunterladen
* Pfad: ffmpeg.org/download.html#build-windows
  * Nutze den Link unter "Windows builds from gyan.dev".
  * Lade die "ffmpeg-git-essentials.7z"-ZIP-Datei herunter.
  * Scanne mit Virustotal: 
  * Entpacke die ZIP-Datei z. B. nach: C:\Entwicklung\ffmpeg\
  * Der Ordner sollte nun etwa so aussehen: C:\Entwicklung\ffmpeg\bin\ffmpeg.exe
* Umgebungsvariable PATH aktualisieren und CMD neu starten (um die Aenderung zu uebernehmen)
  * Umgebungsvariablen öffnen
  * zu PATH => Neu: C:\Entwicklung\ffmpeg\bin\

## requirements installieren
Alle in der requirements.txt genannten Komponenten werden im Code der transcribe.py benötigt und müssen daher vorab installiert sein.

## Stereomix aktivieren und nutzbar machen
* In Windows, bspw. via Rechtsklick auf das Lautsprechersymbol in der Taskleiste, zu den "Soundeinstellungen" wechseln und
  * dort ganz unten "Weitere Soundeinstellungen" öffnen.
  * Den Reiter "Aufnahme" öffnen und 
  * in einen freien Bereich klicken, um "Deaktivierte Geräte anzeigen" zu aktivieren.
* Nun sollte "Stereomix" erschienen sein:
  * Diesen bitte aktivieren und
  * am besten direkt als Standardkommunikationsgerät auswählen.
* Falls USB-Soundgeräte angeschlossen sind, bspw. ein Headset, dies bitte trennen.
* Nun mit dem Standard Windows "Audiorecorder" und gewähltem "Stereomix" als Eingang prüfen, ob das ins Mikrofon gesprochene, sowie bspw. der Text eines abgespielten YouTube-Videos aufgezeichnet werden.

## ID von Stereomix finden
Im Code der transcribe.py ist "print(sd.query_devices())" auskommentiert:
Die Zeile bitte aktivieren und nach Erhalt der Übersicht bpsw. in CMD das Skript mit Strg+C abbrechen.
Nun "device_index=" mit der Hardware-ID des Stereomix versorgen (bei mir ist es die "1")

## Nun kann's losgehen
Nun via python transcribe.py ausprobieren.
Je nach Hardware kann die größe - und damit Qualität - des Whisper-Modells im Code gewählt werden (s. Kommentar):
Ich hatte mich hier für "base" entschieden: model = whisper.load_model("base")
