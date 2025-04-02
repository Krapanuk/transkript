import whisper
model = whisper.load_model('base')
result = model.transcribe('audio.wav', fp16=False)
with open('transkript_full.txt', 'w', encoding='utf-8') as file:
    file.write(result['text'])
print("Transkription abgeschlossen. Der Text wurde in 'transkript_full.txt' gespeichert.")