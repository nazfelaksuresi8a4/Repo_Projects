from mutagen.mp3 import MP3
audio = MP3("dosya.mp3")
print(audio.info.length)  # saniye cinsinden süre (float)
